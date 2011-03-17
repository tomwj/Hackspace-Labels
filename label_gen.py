#! /usr/bin/env python

import os

Laser = ["equipment:lasercutter", "abc123", ["Sol","Russs"], "Laser Cutter", False]
Makerbot = ["equipment:makerbot", "bcd234", ["Sol","Russs", "Glen"], "Makerbot", False]
Washing = ["equipment:washingmachine", "cde345", ["Elliot",], "Washing Machine", False]
Monorail = ["project:monorail", "def456", ["Sol","A. Nother"], "Mono Rail", True]

LHS = [Laser, Makerbot, Washing, Monorail]

device = "Dymo"

Bio = ["project:DIYBio", "123abc", ["Bugs",] "DIY Bio",]

class label(object):
    '''The label class.
    '''
    def __init__(self, data):
        self.link = data[0]
        self.code = data[1]
        self.respMembers = data[2]
        self.itemName = data[3]
        self.Hack = data[4]

    def __call__(self):
        return (self.link, self.code, self.respMembers, self.itemName, self.Hack)

class Printer(object):
    '''Something that is able to take an item, get it's label and print it
        to a physical medium
    '''

    def __init__(self, deviceURI):
        self.device = deviceURI

    def single(self, item):
        itemInfo = item()
        for each in itemInfo:
            print(each)

class item(label):
    '''A class to represent the object to be catalogued
    '''

    def __init__(self, data):
        self.label = label(data)

    def __str__(self):
        out = "\nItem Name: %(name)s\nLink: %(link)s\nResponsible Members: \
%(mem)s\nHack?: %(hack)s\nCode: %(code)s\n" %\
        {"name":self.label.itemName,"link": self.label.link, \
        "mem":self.label.respMembers, "hack":self.label.Hack, "code":self.label.code}

        return out


    def __repr__(self):
        return self.label.itemName

class project(item):
    '''Similar to an item or object, but projects can be linked with items.
    '''

    def __init__(self, details):
        self.items = []
        self.link = None
        self.code = None
        self.Members = []
        self.name = None

    def linkItem(self):
        pass


class space(object):
    ''' The overall container for all components, ie hackSPACE.
    '''

    def __init__(self, datastore):
        self.inventory = {}
        for thing in datastore:
            self.create_item(thing)

        self.printer = Printer(device)

    def make_label(self, item):
        ref = self.inventory[item].label

        print("\nMaking label....\n")
        self.printer.single(ref)

    def listItems(self):
        print("\nItems\n======")
        for thing in self.inventory:
            print(self.inventory[thing])

    def print_label(item):
        self.Printer(item)

    def create_item(self, info):        
        if self.inventory.has_key(info[1]) == True:
            print("Item in Space Inventory")
        else:
            self.inventory[str(info[1])] = item(info)


    def remove_item(self, item):
        self.inventory.pop(item)

London = space(LHS)
#London.listItems()
London.make_label("abc123")

Doorbot = ["equipment:doorbot", "xyz123", ["Sol","Russs", "Mark", "Jonty"], "Doorbot", False]

London.create_item(Doorbot)

London.make_label("xyz123")

London.listItems()
