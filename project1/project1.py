# A stringlist is a list of strings, one of
# "mt" or 
# contains items: Pair(first, rest)
class Pair:
	def __init__(self, first, rest):
		self.first = first
		self.rest = rest

	def __eq__(self, other):
		return ((type(other)==Pair)
			and self.first == other.first
			and self.rest == other.rest
			)

	def __repr__(self):
		return ("Pair ({!r}, {!r})".format(self.first, self.rest))

# a Class Shape contains a name, and a stringlist of field names. One of
# "mt", or 
# contains items - name, strList
class ClassShape:
	def __init__(self, name, strList):
		self.name = name
		self.strList = strList

	def __eq__(self, other):
		return ((type(other) == Pair)
			and self.name == other.name
			and self.strList == other.strList
			)

	def __repr__(self):
		return ("Pair ({!r}, {!r}".format(self.name, self.strList))

# strList -> string
# takes in a list of strings, then joins them into a single string with new lines in between and at the end
def join_lines(strList):
	if strList == "mt":
		return ""
	else:
		return strList.first + "\n" + join_lines(strList.rest)

#strList -> strList
# takes in a list field names, and maps to a strList of line 
def fields_to_assignments(strList):
    if strList == "mt":
        return "mt"
    else:
        return Pair("        self." + strList.first + " = " + strList.first, fields_to_assignments(strList.rest))

#strList -> strList 
# takes in a list of field namses, and maps to a strList of lines
def fields_to_equality(strList):
    if strList == "mt":
        return "mt"
    else:
        return Pair("            and self." + strList.first + " == " + "other." + strList.first, fields_to_equality(strList.rest)) 


#strList -> string
# takes in a string list of field names, and returns a single string where elements are joined with a ", "
def commasep(strList):
    if strList == "mt":
        return ""
    else:
        return ", " + strList.first + commasep(strList.rest) 
#strList -> string
# takes in a string list of field names, and returns a single string where elements are formated for repr method
def commaseprepr(strList):
    if strList == "mt":
        return ""
    else:
        if strList.rest != "mt":
            return "self." + strList.first + ", " + commaseprepr(strList.rest)
        else:
            return "self." + strList.first

#strList -> strList
#takes in a list of field names, and returns a StrList representing the __init__ method
def init_method(strList):
    if strList == "mt":
        return Pair("    def __init__(self):", Pair("        pass", "mt"))
    else:
        return Pair("    def __init__(self"  +  commasep(strList) + "):", fields_to_assignments(strList))

#ClassShape -> strList
#takes in the name of the class and it's field names, and returns a strList representing the equals method
def eq_method(classShape):
    if classShape == "mt":
        return Pair("    def __eq__(self, other):", Pair("        return (type(other) == " + classShape.name, "mt"))
    else:
        return Pair("    def __eq__(self, other):", Pair("        return (type(other) == " + classShape.name, fields_to_equality(classShape.strList)))

#ClassShape -> strList
#takes in a classShape(name, field values), and returns a strList representing the __repr__method
def repr_method(classShape):
    if classShape == "mt":
        return Pair("    def __repr__(self):", Pair('        return "' + classShape.name + '({!r}, {!r})".format()', "mt"))
    else:
        return Pair("    def __repr__(self):", Pair('        return "' + classShape.name + '({!r}, {!r})".format(' + commaseprepr(classShape.strList) + ")", "mt"))

#ClassShape -> string
#takes in a classShape, and returns a single string containing the class definition
def render_class(classShape):
    x = join_lines(init_method(classShape.strList))
    y = join_lines(eq_method(classShape))
    z = join_lines(repr_method(classShape))

    return "class " + classShape.name + ":" + "\n" + x + "\n" + y + "            )" + "\n\n" + z
    

import unittest

class TestCases(unittest.TestCase):

    def test_join_lines(self):
        mylist = "mt"
        self.assertEqual(join_lines(mylist), "")
        strList = Pair("Rent", Pair("is", Pair("due", Pair("tomorrow", "mt"))))
        self.assertEqual(join_lines(strList), "Rent\nis\ndue\ntomorrow\n")
        strList2 = Pair("Name", Pair("a", Pair("more", Pair("iconic", Pair("pair", "mt")))))
        self.assertEqual(join_lines(strList2), "Name\na\nmore\niconic\npair\n")   


    def test_fields_to_assignments(self):
        mylist = "mt"
        self.assertEqual(fields_to_assignments(mylist), "mt")
        strList = Pair("x", Pair("y", "mt"))
        self.assertEqual(fields_to_assignments(strList), Pair("        self.x = x", Pair("        self.y = y", "mt")))
       

    def test_fields_to_equality(self):
        mylist = "mt"
        self.assertEqual(fields_to_equality(mylist), "mt")
        strList = Pair("x", Pair("y", "mt"))
        self.assertEqual(fields_to_equality(strList), Pair("            and self.x == other.x", Pair("            and self.y == other.y", "mt")))
       

    def test_commasep(self):
        mylist = "mt"
        self.assertEqual(commasep(mylist), "")
        strList = Pair("x", Pair("y", "mt"))
        self.assertEqual(commasep(strList), ", x, y")
       

    def test_commaseprepr(self):
        mylist = "mt"
        self.assertEqual(commaseprepr(mylist), "")
        strList = Pair("x", Pair("y", "mt"))
        self.assertEqual(commaseprepr(strList), "self.x, self.y")

    def test_init_method(self):
        mylist = "mt"
        self.assertEqual(init_method(mylist), Pair("    def __init__(self):", Pair("        pass", "mt")))
        strList = Pair("x", Pair("y", "mt"))
        self.assertEqual(init_method(strList), Pair("    def __init__(self, x, y):", Pair("        self.x = x", Pair("        self.y = y", "mt"))))
        
    def test_eq_method(self):
        myClass = ClassShape("Computer", "mt")
        self.assertEqual(eq_method(myClass), Pair("    def __eq__(self, other):", Pair("        return (type(other) == Computer", "mt")))
        className = ClassShape("Point", Pair("x", Pair("y", "mt")))
        self.assertEqual(eq_method(className), Pair("    def __eq__(self, other):", Pair("        return (type(other) == Point", Pair("            and self.x == other.x", Pair("            and self.y == other.y", "mt")))))
        

    def test_repr_method(self):
        myClass = ClassShape("Computer", "mt")
        self.assertEqual(repr_method(myClass), Pair("    def __repr__(self):", Pair('        return "Computer({!r}, {!r})".format()', "mt")))
        className = ClassShape("Point" , Pair("x", Pair("y", "mt")))
        self.assertEqual(repr_method(className), Pair('    def __repr__(self):', Pair('        return "Point({!r}, {!r})".format(self.x, self.y)', "mt")))

    def test_render_class(self):
        className = ClassShape("Plate", Pair("diameter", Pair("material", "mt")))
        self.assertEqual(render_class(className), 'class Plate:\n    def __init__(self, diameter, material):\n        self.diameter = diameter\n        self.material = material\n\n    def __eq__(self, other):\n        return (type(other) == Plate\n            and self.diameter == other.diameter\n            and self.material == other.material\n            )\n\n    def __repr__(self):\n        return "Plate({!r}, {!r})".format(self.diameter, self.material)\n')


if __name__ == '__main__':
    unittest.main()