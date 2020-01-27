"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Hameedah Khadar [hjk63]
Date:   25 Sept 2019
"""
import introcs
import a1

def testA():
    """
    Test functions before_space(), after_space()
    """

    #testing one space
    atest1= a1.before_space('Hameedah Khadar')
    introcs.assert_equals('Hameedah', atest1)

    #testing multiple spaces
    atest2= a1.before_space('Ham   Khadar')
    introcs.assert_equals('Ham', atest2)

    #testing spaces in the beginning of the string
    atest3= a1.before_space(" HelloWorld")
    introcs.assert_equals("" , atest3)

    #testing multiple seperated spaces
    atest8= a1.before_space('Hello World !')
    introcs.assert_equals("Hello", atest8)

    #testing one space
    atest5= a1.after_space('Hameedah Khadar')
    introcs.assert_equals('Khadar', atest5)

    #testing multiple spaces
    atest6= a1.after_space('Ham   Khadar')
    introcs.assert_equals('  Khadar', atest6)

    #testing spaces in the beginning of the string
    atest7= a1.after_space(" HelloWorld!")
    introcs.assert_equals("HelloWorld!" , atest7)

    #testing multiple seperated spaces
    atest9= a1.after_space('Hello World !')
    introcs.assert_equals("World !", atest9)

    #testing space in the end of the string
    atest10= a1.after_space("HelloWorld ")
    introcs.assert_equals("" , atest10)


def testB():
    """
    Test functions get_src(), get_dst()
    """

    #testing one occurrence of double quotes
    btest1= a1.first_inside_quotes('A "BD" D')
    introcs.assert_equals("BD" , btest1)

    #testing multiple occurrence of double quotes
    btest2= a1.first_inside_quotes('A b "cde" fg "hi" jk ')
    introcs.assert_equals("cde" , btest2)

    #testing nothing in the double quote
    btest3= a1.first_inside_quotes('""')
    introcs.assert_equals("" , btest3)

    #testing a string with only double quotes
    btest4= a1.first_inside_quotes('"ab"')
    introcs.assert_equals("ab" , btest4)

    #testing a valid input
    btest5=a1.get_lhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 '+
    'Euros","err":"" }')
    introcs.assert_equals('1 Bitcoin' , btest5)

    #testing an invalid input
    btest7=a1.get_lhs('{ "ok":false, "lhs":"", "rhs":"", "err":"Source '+
    'currency code is invalid." }')
    introcs.assert_equals('' , btest7)

    #testing an invalid input
    btest8=a1.get_rhs('{ "ok":false, "lhs":"", "rhs":"", "err":"Source '+
    'currency code is invalid." }')
    introcs.assert_equals('' , btest8)

    #testing a valid input
    btest9=a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 '+
    'Euros","err":"" }')
    introcs.assert_equals('9916.0137 Euros' , btest9)

    #testing an invalid query
    btest10=a1.has_error('{ "ok":false, "lhs":"", "rhs":"", "err":"" }')
    introcs.assert_equals(True , btest10)

    #testing a valid query
    btest11=a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 '+
    'Euros", "err":"" }')
    introcs.assert_equals(False , btest11)

    #testing an invalid currency
    btest11=a1.has_error('{ "ok":false, "lhs":"", "rhs":"", '+
    '"err":"Exchange currency code is invalid." }')
    introcs.assert_equals(True , btest11)


def testC():
    """
    Test functions currency_response()
    """

    #testing converting to the same currency
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 Australian Dollars",'+
    ' "rhs":"2.5 Australian Dollars", "err":""'+
    ' }', a1.currency_response("AUD","AUD",2.5))

    #testing converting between 2 different currencies
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 Australian Dollars",'+
    ' "rhs":"1.7551668602031 United States Dollars", "err":"" }'+
    '', a1.currency_response("AUD","USD",2.5))

    #testing invalid source currency
    introcs.assert_equals('{ "ok":false, "lhs":"", "rhs":"", "err":"Source '+
    'currency code is invalid." }', a1.currency_response("abc","USD",2.5))

    #testing 2 invalid currencies
    introcs.assert_equals('{ "ok":false, "lhs":"", "rhs":"", "err":"Source'+
    ' currency code is invalid." }', a1.currency_response("abc","def",2.5))

    #testing invalid exchange currency
    introcs.assert_equals('{ "ok":false, "lhs":"", "rhs":"", "err":"'+
    'Exchange currency code is invalid.'+
    '" }', a1.currency_response("USD","def",2.5))


def testD():
    """
    Test functions iscurrency(), and exchange()
    """

    #test valid currency
    introcs.assert_true(a1.is_currency("USD"))

    #test invalid currency
    introcs.assert_equals(False, a1.is_currency("ABC"))

    #test invalid currency (>3 letters)
    introcs.assert_equals(False, a1.is_currency("invalid"))

    #test invalid currency (<3 letters)
    introcs.assert_equals(False, a1.is_currency("hi"))

    #testing a valid currency to a different valid currency
    introcs.assert_equals(64.375, a1.exchange("USD", "CUP", 2.5))

    #testing a valid to itself
    introcs.assert_equals(2.5, a1.exchange("USD", "USD", 2.5))

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
