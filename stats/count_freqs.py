#!/usr/bin/python
"""
Author: Diggory <diggory.hardy@gmail.com>
Date: August 2011

Count sequence frequencies found in all input files/dirs. Assumes all files
are textual. With a few basic rules, this works very well to construct a list
of sequences it might be useful to use on a chorded keyboard. Rules:
1.  Throw out any sequences containing whitespace
2.  Throw out any sequences where frequency*length/doc-length is less than the
    cut-off.
3.  For every sequence, throw out any sub-sequences which have a lower score
    (frequency*length) than the parent sequence.

Bug: sequencies which repeat themselves may get counted too many times. E.g. in
"abcabcabc", the sequence "abc" would (correctly) be matched 3 times, but
"abcabc" would be matched twice instead of once. This probably causes things
like "---" to get much too high frequencies in markdown documents.

Limitation: all results are either case sensitive or insensitive depending on
options: "the" and "The" and "THE" are either all considered the same or all
considered different sequences. Depending on usage this may not be desired.

My usage (where ../mongrel countains many markdown text files):

./count_freqs.py -g "*.md" -l80 ../mongrel/ > mongrel-freqs.txt

Note: status messages are printed to stderr, so should appear even with
redirection.
"""
import os
import sys
import fnmatch
from optparse import OptionParser

'''
Old notes before implementing brute-force sequence counting. I was this method
would perform badly, but it appears fine; notes can stay in case with larger
inputs this does become a problem.

This only scans single character frequencies.
To extend to look for frequent pairs and longer sequences, we could:

*   Use a brute-force approach (log frequency of every pair). This may be
    doable for pairs, but becomes unreasonable when looking for longer sequences.
*   Cut-down brute-force: look at all combinations of a set-length which are
    composed of two sequences one character shorter whose popularity is above
    a certain level. This requires a re-scan for each deepening level.
*   Use hash sequences. Generate some hash for fixed-length combinations and
    tot up hash frequencies. Parse texts again, storing the sequences of the
    most frequent hashes and counting their frequencies. For short sequences
    this is probably pointless, but for larger ones it limits the size of the
    hash of frequencies needing recording in a probably more computationally
    efficient mannor to the above.

This could be used to produce a table of top frequencies per sequence length,
or to produce a single table of the top, say 1000, sequences of any length.
'''
class StatCounter:
    def __init__(self,length):
        self.seqFreqs=dict()
        self.textLen=0
        self.length=length
    def scan(self,line,caseSens):
        if caseSens:
            uline=unicode(line,'utf-8','ignore')
        else:
            uline=unicode(line,'utf-8','ignore').lower()
        self.textLen+=len(uline)
        for l in range(1,self.length+1):
            for i in xrange(0,len(uline)+1-l):
                seq=uline[i:i+l]
                if not (' ' in seq or '\t' in seq or '\n' in seq):
                    if seq in self.seqFreqs:
                        self.seqFreqs[seq]+=1
                    else:
                        self.seqFreqs[seq]=1
    def display(self,cutOff):
        print >>sys.stderr, "Got",len(self.seqFreqs),"sequences, removing ones below cut-off..."
        print "   freq\t  % doc\tsequence"
        initialNum=len(self.seqFreqs)
        for seq,freq in self.seqFreqs.items():
            #remove low-frequency entries
            if len(seq)*freq<cutOff*self.textLen:
                del self.seqFreqs[seq]
        print >>sys.stderr, "Got",len(self.seqFreqs),"sequences, removing redundant subsequences..."
        for seq,freq in self.seqFreqs.items():
            #try to remove some of the useless entries
            score=freq*len(seq)
            for subseq,ssfreq in self.seqFreqs.items():
                if seq.find(subseq)>=0:
                    if score>ssfreq*len(subseq):
                        del self.seqFreqs[subseq]
        pcFreq=list()
        print >>sys.stderr, "Got",len(self.seqFreqs),"sequences, printing..."
        for seq,freq in self.seqFreqs.iteritems():
            pcFreq.append( (freq, float(freq)*len(seq), seq) )
        def valCmp(a,b):
            x,u,s=a
            y,v,t=b
            return cmp(y,x)
        pcFreq.sort(valCmp)
        for freq,score,seq in pcFreq:
            print "{0: >7}\t{1: >7.2%}\t".format(freq,score/self.textLen)+seq.encode('unicode_escape')
        print "{0} unique sequences; {1} printed; {2} total characters".format(initialNum,len(self.seqFreqs),self.textLen)

def main(args):
    parser = OptionParser(usage="Usage: %prog [options] PATHS",
            description="""Collects character stats from PATHS (recursively)""")
    
    parser.add_option("-g","--glob",
            action="append", dest="glob", default=list(),
            help="Only parse files matching this glob (argument may be given multiple times to give more globs)")
    parser.add_option("-l","--length",
            action="store", type="int", dest="length", default=1,
            help="Match sequences up to this length. Note that since sequences containing whitespace are eliminated early, increasing this to 20 or so is quite a good idea. Default: 1")
    parser.add_option("-o","--cutoff",
            action="store", type="float", dest="prop", default=0.001,
            help="Only display entries which constitute at least this proportion of the text (default 0.001)")
    parser.add_option("-c","--case-sensitive",
            action="store_true", dest="caseSens", default=False,
            help="Consider the, The and THE different sequences")
    (options, others) = parser.parse_args(args=args)
    
    print >>sys.stderr, "Looking for files..."
    files=set()
    for path in others:
        if os.path.isfile(path):
            files.add(os.path.abspath(path))
        elif os.path.isdir(path):
            for dirpath,subdirs,subfiles in os.walk(path):
                for subfile in subfiles:
                    if len(options.glob)==0:
                        files.add(os.path.abspath(os.path.join(dirpath,subfile)))
                    else:
                        for glob in options.glob:
                            if fnmatch.fnmatch(subfile,glob):
                                files.add(os.path.abspath(os.path.join(dirpath,subfile)))
                                break
    
    print >>sys.stderr, "Got",len(files),"files, scanning for sequences..."
    stats=StatCounter(options.length)
    for fpath in files:
        f=open(fpath)
        for line in f:
            stats.scan(line,options.caseSens)
        f.close()
    
    stats.display(options.prop)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
