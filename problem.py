import pylab, math

# def maxVal(w, v, i, aW):
# 	# print 'maxVal called with : ', i, aW
# 	global numCalls
# 	numCalls += 1
# 	if i==0:
# 		if w[i] <= aW: return v[i]
# 		else: return 0
# 	without_i = maxVal(w, v, i-1, aW)
# 	if w[i] > aW:
# 		return without_i
# 	else: 
# 		with_i = v[i] + maxVal(w, v, i-1, aW - w[i])
# 	return max(with_i, without_i)

# def fastMaxVal(w, v, i, aW, m):
# 	global numCalls
# 	numCalls += 1
# 	try: return m[(i, aW)]
# 	except KeyError:
# 		if i == 0:
# 			if w[i] <= aW:
# 				m[(i, aW)] = v[i]
# 				return v[i]
# 			else:
# 				m[(i, aW)] = 0
# 				return 0
# 		without_i = fastMaxVal(w, v, i-1, aW, m)
# 		if w[i] > aW:
# 			m[(1, aW)] = without_i
# 			return without_i
# 		else:
# 			with_i = v[i] + fastMaxVal(w, v, i-1, aW - w[i], m)
# 		res = max(with_i, without_i)
# 		m[(i, aW)] = res
# 		return res

# def maxVal0(w, v, i, aW):
# 	m = {}
# 	return fastMaxVal(w, v, i, aW, m)

# weights = [1, 1, 5, 5, 3, 3, 4, 4]
# vals = [15, 15, 10, 10, 9, 9, 5, 5]
# numCalls = 0
# aW = 8
# res = maxVal(weights, vals, len(vals) -1, aW)
# print 'max Val = ', res, ', number of calls = ', numCalls
# numCalls = 0
# res = maxVal0(weights, vals, len(vals) -1, aW)
# print 'max Val0 = ', res, ', number of calls = ', numCalls

# # def maxValO(w, v, i, aW):
# # 	m = ()
# # 	return fastMaxVal(w, v, i, aW, m)
#  # def maxVal(w, v, i, aW):
# 	# weights = [1, 1, 5, 5, 3, 3, 4, 4]
# 	# vals = [15, 15, 10, 10, 9, 9, 5, 5]
# 	# numCalls = 0
# 	# res = maxVal(weights, vals, len(vals) - 1, 8)
# 	# 	print ('max Val', res, 'number of calls', numCalls)
# 	# assert False
# 	# 	print('maxVal called with', i, aW)


# def fib(n):
# 	global numCalls
# 	numCalls += 1
# 	# print 'fib called with', n
# 	if n <= 1:
# 		return n
# 	else:
# 		return fib(n-1) + fib(n-2)

# numCalls = 0
# n = 40
# print 'fib of', n, ' = ', fib(n)
# print 'numCalls =', numCalls


# def fib1(n):
# 	global memo
# 	global numCalls
# 	numCalls += 1
# 	if not n in memo:
# 		memo[n] = fib1(n-1) + fib1(n-2)
# 	return memo[n]

# memo = {0:0, 1:1}
# numCalls = 0
# n = 40
# print 'fib of', n, '=', fib1(n)
# print 'numCalls =', numCalls

##power (x, n)
# def pow(x, n):
# 	global numCalls
# 	numCalls += 1
# 	if n == 0:
# 		return 1
# 	else:
# 		return x*pow(x, n-1)

# numCalls = 0
# x = 2
# n = 31
# print 'Power of ', x, ' to ', n, ' = ', pow(x, n)
# print 'numCalls =', numCalls

##power2
# def Pow(x,n):
# 	global numCalls
# 	numCalls += 1
# 	if n == 0:
# 		return 1
# 	elif n%2 == 0:
# 		y = Pow(x, n/2)
# 		return y*y
# 	else: return x*Pow(x, n-1)

# numCalls = 0
# x = 100000
# n = 49
# print 'Power of ', x, ' to ', n, ' = ', Pow(x, n)
# print 'numCalls =', numCalls

##modular exponentiation - using recursion
# def Mod(x, n, M):
# 	if n == 0: return 1
# 	elif n%2 == 0:
# 		y = Mod(x, n/2, M)
# 		return (y*y) %M
# 	else:
# 		return ((x%M) * Mod(x, n-1, M)) %M

# numCalls = 0
# x = 5
# n = 3 
# M = 7
# print 'Modulo ',M, ' of ',x, ' exponent ',n, ' = ', Mod(x, n, M)
# # print 'numCalls =', numCalls


#### points as lists : Lecture 15

# def addPoints(p1, p2):
# 	r =[]
# 	r.append(p1[0]+p2[0])
# 	r.append(p1[1]+p2[1])
# 	return r

# p = [1, 2]
# q = [3, 1]
# r = addPoints(p,q)
# print r

#### points as classes

# class cartesianPoint:
# 	pass

# cp1 = cartesianPoint()
# cp2 = cartesianPoint()
# cp1.x = 1.0
# cp1.y = 2.0
# cp2.x = 1.0
# cp2.y = 3.0

# def samePoint(p1, p2):
# 	return (p1.x == p2.x) and (p1.y == p2.y)

#####################
# p1 = cartesianPoint()
# p1.x = 3
# p1.y = 4
# p2 = cartesianPoint()
# p2.x = 3
# p2.y = 4
# # print p1 is p2
# print samePoint(p1, p2)
# p = 6
# print printPoint()
# print cp2.y

 
# def printPoint(p):
#  	print '(' + str(p.x) + ', ' + str(p.y) + ' )'

# class polarPoint:
# 	pass
# pp1 = polarPoint()
# pp2 = polarPoint()
# pp1.radius = 1.0
# pp1.angle = 0
# pp2.radius = 2.0
# pp2.angle = math.pi / 4.0

# # print pp1 is pp2


# class cPoint(object):
# 	"""docstring for cPoint"""
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# 		self.radius = math.sqrt(self.x*self.x + self.y*self.y)
# 		self.angle = math.atan2(self.y, self.x)
# 	def cartesian(self):
# 		return (self.x, self.y)
# 	def polar(self):
# 		return (self.radius, self.angle)
# 	def __str__(self):
# 		return '(' + str(self.x) + ', '+str(self.y)+ ' )'
# 	def __cmp__(self, other):
# 		return (self.x > other.x) and (self.y > other.y)

# p = cPoint(1.0, 2.0)
# # print p.cartesian()
# # print p.polar()
# # print p.x = 'foobar'
# # print p.y
# # print p.radius
# # print p.angle

# class pPoint(object):
# 	"""docstring for pPoint"""
# 	def __init__(self, r, a):
# 		self.radius = r
# 		self.angle = a
# 		self.x = r * math.cos(a)
# 		self.y = r * math.sin(a)
# 	def cartesian(self):
# 		return (self.x, self.y)
# 	def polar(self):
# 		return (self.radius, self.angle)
# 	def __str__(self):
# 		return '(' + str(self.x) + ', ' + str(self.y) + ' )'
# 	def __cmp__(self, other):
# 		return (self.x > other.x) and (self.y > other.y)

# p.radius = 5.0
# # print p.cartesian()
# # print p.polar()

# q = pPoint(3.0, 4.0)
# # print p > q
# # print dir(p)


# class Segment:
# 	"""docstring for Segment"""
# 	def __init__(self, start, end):
# 		self.start = start
# 		self.end = end
# 	def length(self):
# 		return math.sqrt( ((self.start.x - self.end.x) * (self.start.x - self.end.x))
# 						+ ((self.start.y - self.end.y) * (self.start.y - self.end.y)))

# p1 = cPoint(3.0, 4.0)
# p2 = cPoint(5.0, 7.0)
# s1 = Segment(p1, p2)
# print s1.length()

















#### Lecture 17
# class Location(object):
# 	def __init__(self, x, y):
# 		self.x = float(x)
# 		self.y = float(y)
# 	def move(self, xc, yc):
# 		return Location(self.x+float(xc), self.y+float(yc))
# 	def getCoords(self):
# 		return self.x, self.y
# 	def getDist(self, other):
# 		ox, oy = other.getCoords()
# 		xDist = self.x - ox
# 		yDist = self.y - oy
# 		return math.sqrt(xDist**2 + yDist**2)

# class CompassPt(object):
# 	possibles = ('N', 'S', 'E', 'W')
# 	def __init__(self, pt):
# 		if pt in self.possibles: self.pt = pt
# 		else: raise ValueError('in CompassPt.__init__')
# 	def move(self, dist):
# 		if self.pt == 'N': return (0, dist)
# 		elif self.pt == 'S': return (0, -dist)
# 		elif self.pt == 'E': return (dist, 0)
# 		elif self.pt == 'W': return (-dist, 0)
# 		else: raise ValueError('in CompassPt.move')

# class Field(object):
# 	def __init__(self, drunk, loc):
# 		self.drunk = drunk
# 		self.loc = loc
# 	def move(self, cp, dist):
# 		oldLoc = self.loc
# 		xc, yc = cp.move(dist)
# 		self.loc = oldLoc.move(xc, yc)
# 	def getLoc(self):
# 		return self.loc
# 	def getDrunk(self):
# 		return self.drunk

# class Drunk(object):
# 	def __init__(self, name):
# 		self.name = name
# 	def move(self, field, time = 1):
# 		if field.getDrunk() != self:
# 			raise ValueError('Drunk.move called with drunk not in field')
# 			for i in range(time):
# 				pt = CompassPt(random.choice(CompassPt.possibles))
# 				field.move(pt, 1)
# 	def performTrial(time, f):
# 		start = f.getLoc()
# 		distances = [0.0]
# 		for t in range(1, time + 1):
# 			f.getDrunk().move(f)
# 			newLoc = f.getLoc()
# 			distance = newLoc.getDist(start)
# 			distances.append(distance)
# 			return distances
# 			drunk = Drunk('Homer Simpson')
# 		for i in range(3):
# 			f = Field(drunk, Location(0, 0))
# 			distances = performTrial(500, f)
# 			pylab.plot(distances)
# 			pylab.title('Homer\'s Random Walk')
# 			pylab.xlabel('Time')
# 			pylab.ylabel('Distance from Origin')

# 	def performSim(time, numTrials):
# 		distLists = []
# 		for trial in range(numTrials):
# 			d = Drunk('Drunk' + str(trial))
# 			f = Field(d, Location(0, 0))
# 			distances = performTrial(time, f)
# 			distLists.append(distances)
# 			return distLists
# 	def ansQuest(maxTime, numTrials):
# 		means = []
# 		distLists = performSim(maxTime, numTrials)
# 		for t in range(maxTime + 1):
# 			tot = 0.0
# 		for distL in distLists:
# 			tot += distL[t]
# 			means.append(tot/len(distL))
# 			pylab.figure()
# 			pylab.plot(means)
# 			pylab.ylabel('distance')
# 			pylab.xlabel('time')
# 			pylab.title('Average Distance vs. Time (' + str(len(distLists)) + ' trials)')
# 			ansQuest(500, 300)
# 			pylab.show()



#### Lecture 16
class Person(object):
	"""docstring for Person"""
	def __init__(self, family_name, first_name):
		self.family_name = family_name
		self.first_name = first_name
	def familyName(self):
		return self.family_name
	def firstName(self):
		return self.first_name
	def __cmp__(self, other):
		return cmp((self.family_name, self.first_name), (other.family_name, other.first_name))
	def __str__(self):
		return '<Person: %s %s>'%(self.family_name, self.first_name)
	def say(self,toWhom,something):
		return self.first_name + ' ' + self.family_name + ' says to ' + toWhom.familyName() + ' ' + toWhom.firstName() + ': ' + something
	def sing(self, toWhom, something):
		return self.say(toWhom,something+ 'tra la la')

pers = Person('Dizele', 'Kafutshi')
# print m
# print 'My name is : ' + pers.familyName() + ' ' + pers.firstName()
# print pers.say(pers, 'Why do you know thing about me?')
# print pers.sing(pers, 'Lay me down - Sam Smith ')


class MITPerson(Person):
	nextIdNum = 0
	"""docstring for MITPerson"""
	def __init__(self, familyName, firstName):
		Person.__init__(self, familyName, firstName)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __str__(self):
		return '<MIT Person: %s %s>'%(self.first_name, self.family_name)
	def __cmp__(self, other):
		return cmp(self.idNum, other.idNum)

p1 = MITPerson('Sam', 'Smith')
p2 = MITPerson('Chris', 'Benoit')
# print p1.getIdNum()
# print p2.getIdNum()
# print p1
# print p2

class UG(MITPerson):
	"""docstring for UG"""
	def __init__(self, familyName, firstName):
		MITPerson.__init__(self, familyName, firstName)
		self.year = None
	def setYear(self, year):
		if year > 5: raise OverflowError('Too many')
		self.year = year
	def getYear(self):
		return self.year
	def say(self,toWhom,something):
		return MITPerson.say(self,toWhom,'Excuse me, but ' + something)

aaron = Person("Grimson", "Eric")
ug = UG('Doe', 'Jane')
year = ug.setYear(4)
# print ug.getYear()
# print ug.getIdNum()
# print me.familyName()
# print ug.say(pers,'I appreciate you so much!')
# print pers > ug

class Prof(MITPerson):
	"""docstring for Prof"""
	def __init__(self, familyName, firstName, rank):
		MITPerson.__init__(self, familyName, firstName)
		self.rank = rank
		self.teaching = {}
	def addTeaching(self, term, subj):
		try:
			self.teaching[term].append(subj)
		except KeyError:
			self.teaching[term] = [subj]
	def getTeaching(self, term):
		try:
			return self.teaching[term]
		except KeyError:
			return None
	def lecture(self,toWhom,something):
		return self.say(toWhom,something + ' as it is obvious')
	def say(self,toWhom,something):
		if type(toWhom) == UG:
			return MITPerson.say(self,toWhom,'I do not understand why you say '+something)
		elif type(toWhom) == Prof:
			return MITPerson.say(self,toWhom,'I really liked your paper on ' +something)
		else:
			return self.lecture(something)


me = Prof('Derek', 'Banas', 'Full')
# print me.lecture(ug,'J\'ai envie de toi')
# me.addTeaching('F08', 'Math')
# me.addTeaching('S09', 'Physics')
# me.addTeaching('E05', 'Biology')
# me.addTeaching('A03', 'History')
# me.addTeaching('H05', 'Geography')
# me.addTeaching('Z09', 'Archeology')
# print me.getTeaching('F08')
# print me.getTeaching('S09')
# print me.getTeaching('H05')

class Faculty(object):
	"""docstring for Faculty"""
	def __init__(self):
		self.names = []
		self.IDs = []
		self.members = []
		self.place = None
	def add(self,who):
		if type(who) != Prof: raise TypeError('not a professor')
		if who.getIdNum() in self.IDs: raise ValueError('duplicate ID')
		self.names.append(who.familyName())
		self.IDs.append(who.getIdNum())
		self.members.append(who)
	def __iter__(self):
		self.place = 0
		return self
	def next(self):
		if self.place >= len(self.names):
			raise StopIteration
		self.place += 1
		return self.members[self.place-1]

grimson = Prof('Grimson','Eric', 'Full')
lozano = Prof('Lozano-Perez', 'Tomas', 'Full')
guttag = Prof('Guttag', 'John', 'Full')
barzilay = Prof('Barzilay', 'Regina', 'Associate')
course6 = Faculty()
course6.add(grimson)
course6.add(lozano)
course6.add(guttag)
course6.add(barzilay)

for p in course6:
	print p.familyName()

print ug.say(grimson,'I do not understand')
print grimson.say(ug,'you do not understand')
print grimson.say(guttag,'why the sky is blue')

print ug.sing(ug,'I think I finally understand')