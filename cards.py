# coding: utf-8
import random

class deck:
   def __init__(self, N=40, face=True):
      self.N = N
      self.cards = range(1, self.N + 1) #40 cards
      assert N >= 4, "There must be at least one card per suit"
      self.degree = self.N/4
      self.face = face 

   def shuffle(self):
      random.shuffle(self.cards)

   def pop(self):
      try:
         return self.cards.pop()
      except:
         return None

   def extractByValue(self, v):
      for i in self.cards:
         if self.value(i) == v:
            self.cards.remove(i)
            return i
      return None

   def merge(self, d):
      assert d.degree == self.degree
      try:
         self.cards.extend(d.cards)
      except:
         print "Merging not possible"

   def reshuffle(self, card):
      self.cards.append(card)
      self.shuffle()

   def reset(self):
      self.cards = range(1, self.N + 1)
      self.shuffle()

   def suit(self, i):
      suits = u'♠♣♥♦'
      s = (i-1)/self.degree
      try:
         return suits[s]
      except:
         return '*'

   def value(self, i):
      value = (i-1)%self.degree + 1
      if self.suit(i) != '*' and self.face == True:
         if value == 1:
            return 'A'
         if value == self.degree-2:
            return 'J'
         if value == self.degree-1:
            return 'Q'
         if value == self.degree:
            return 'K'
      return value

   def display(self):
      for i in self.cards:
         print self.pretty(i),
      print ''

   def pretty(self, i):
      try:
         return self.suit(i) + " " + str(self.value(i))# + " ("+str(i)+")"
      except:
         return "Nada"


#TODO generator

def runTest(N,game, *args):
   success = 0
   chunk = N/10
   for i in xrange(N):
      if i%chunk == 0:
         print "."
      if game(*args) == True:
         success += 1
   print success, 100*float(success)/N


def play123(verbose=False):

   d = deck(40, face=False)
   d.shuffle()
   card = d.pop()
   i = 0
   while card is not None:
      i += 1
      if verbose:
         print i, d.pretty(card) 
      if d.value(card) == i%3:
         return False
      card = d.pop()

   # Success!
   return True

def pyramid(depth):
   N = 40
   assert depth*(depth+1)/2 < N
   
   d = deck(N, face=False)
   d.shuffle()

   # Building phase

   levels = []
   hidden = []

   for l in xrange(depth):
      levels.append([])
      size = l+1
      for x in xrange(size):
         levels[l].append(d.pop())
      print levels[l]

   # Check if the card is free
   def isfree(lev,index):
      if lev == depth-1:
         return True
      if levels[lev+1][index] == None and levels[lev+1][index + 1] == None:
         return True
      else:
         return False

   # Play!
   found = True 
   while found == True:
      found = False
      print "Deck:", 
      d.display()
      for l in xrange(depth):
         print levels[l]

      for l in xrange(depth):
         for i,x in enumerate(levels[l]):
            if x is None or not isfree(l,i):
               continue
            print "Open:",d.pretty(x) #, l, i, x
            value = d.value(levels[l][i])
            if value == 10:
               found = True
               levels[l][i] = None
               continue 
            card = d.extractByValue(10 - value)
            if card is not None:
               print "Extracted:",d.pretty(card)
               found = True 
               levels[l][i] = None

   for l in xrange(depth):
      for x in levels[l]:
            if x is not None:
               return False

   return True

