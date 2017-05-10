# -*- coding: utf-8 -*-
"""
Created on Mon May  8 17:03:51 2017

@author: Andrew
"""
from random import randint,choice,sample

# We need to set up candidates to vote for and then generate a bunch of voters with preferences

# Candidates are just labels. Also have a list of them
Candidates = []

class Candidate:
    def __init__(self,name):
        self.name = name
        Candidates.append(self)
        
fox = Candidate('Fox')
speed = Candidate('Speed')
conway = Candidate('Conway')

# Voters have the candidate they wish to vote for, plus optional apathy and honesty for later
class Voter:
    def __init__(self,vote,apathy=0,honesty=100):
        self.vote = vote
        self.apathy = apathy
        self.honesty = honesty
        
def generate_population_without_apathy(x,y):
    pop = []
    number = 0
    while number < x:
        pop.append(Voter(fox))
        number = number + 1
    while number < x + y:
        pop.append(Voter(speed))
        number = number + 1
    return pop

# election takes in a population, builds a list of votes and then records and prints totals.
def election(pop):
    votes = []
    options = []
    result = {}
    for voter in pop:
        votes.append(voter.vote)
    for option in votes:
        if option in options:
            pass
        else:
            options.append(option)
            result[option.name] = votes.count(option)
            print(option.name + ' got ' +  str(votes.count(option)) + ' votes.')
    return result


def generate_population_with_two(x,y):
    pop = []
    for number in range(x):
        pop.append(Voter(fox,randint(1,100),randint(1,100)))
    for number in range (y):
        pop.append(Voter(speed,randint(1,100),randint(1,100)))
    return pop

def generate_population(x,y,z):
    pop = []
    for number in range(x):
        pop.append(Voter(fox,randint(1,100),randint(1,100)))
    for number in range(y):
        pop.append(Voter(speed,randint(1,100),randint(1,100)))
    for number in range(z):
        pop.append(Voter(conway,randint(1,100),randint(1,100)))
        
    return pop

def election_with_apathy(pop,threshold):
    votes = []
    options = []
    result = {}
    for voter in pop:
        if voter.apathy > threshold:
            votes.append(voter.vote)
        else:
            pass
    for option in votes:
        if option in options:
            pass
        else:
            options.append(option)
            result[option.name] = votes.count(option)
            print(option.name + ' got ' +  str(votes.count(option)) + ' votes.')
    return result


def honest_opinion_poll(pop,samplesize):
    if samplesize > len(pop):
        print('That sample is larger than the population.')
    else:
        poll = sample(pop,samplesize)
        votes = []
        options = []
        result = {}
        for voter in poll:
            votes.append(voter.vote)
        for option in votes:
            if option in options:
                pass
            else:
                options.append(option)
                result[option.name] = votes.count(option)
                print(option.name + ' got ' +  str(votes.count(option)) + ' votes out of ' + str(len(poll)) + '.')
        return result
        

# now an opinion poll with lies allowed
def opinion_poll(pop,samplesize,honestythreshold):
    if samplesize > len(pop):
        print('That sample is larger than the population.')
    else:
        poll = sample(pop,samplesize)
        votes = []
        options = []
        result = {}
        for voter in poll:
            if voter.honesty >= honestythreshold:
                votes.append(voter.vote)
            else:
                votes.append(choice(Candidates))
        for option in votes:
            if option in options:
                pass
            else:
                options.append(option)
                result[option.name] = votes.count(option)
                print(option.name + ' got ' +  str(votes.count(option)) + ' votes out of ' + str(len(poll)) + '.')
        return result
    
testpop = generate_population(500,500,200)
election(testpop)
a = election_with_apathy(testpop,20)
honest_opinion_poll(testpop,100)
opinion_poll(testpop,100,10)
opinion_poll(testpop,200,10)
print(a)