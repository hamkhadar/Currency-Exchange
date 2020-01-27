"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Hameedah Khadar [hjk63]
Date:   25 Sept 2019
"""
import introcs

def before_space(s):
    '''Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space'''

    firstspace = s.index(' ')
    everythingbefore= s[:firstspace]
    return everythingbefore


def after_space(s):
    '''Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space'''

    firstspace = s.index(' ')
    everythingafter= s[firstspace+1:]
    return everythingafter


def first_inside_quotes(s):
    '''Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes'''


    q1 = s.find('"')
    q2 = s.find('"', q1 + 1)
    return s[q1 +1:q2]


def get_lhs(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''

    f1 = json.index("lhs")
    cut_it = json[f1+4:]
    f2 = first_inside_quotes(cut_it)
    return f2


def get_rhs(json):
    '''Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''

    find= json.index("rhs")
    cut_2 = json[find+4:]
    find1= first_inside_quotes(cut_2)
    return find1


def has_error(json):

    '''Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "ok". For example,
    if the JSON is

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''

    w= json.index("ok")
    cut1= json[w:]
    other= cut1.find("false")
    return other!= -1


def currency_response(src, dst, amt):
    '''Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "ok" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float'''


    url="http://cs1110.cs.cornell.edu/2019fa/a1?src=" +src+ "&dst=" +dst+ "&amt=" +str(amt)
    result = introcs.urlread(url)
    return result



def is_currency(code):

    '''Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.'''
    return not has_error(currency_response("USD", code, 2.5))


def exchange(src, dst, amt):
    '''Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency
    src to the currency dst. The value returned represents the
    amount in currency dst.

    The value returned has type float.

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float'''

    part1= get_rhs(currency_response(src, dst, amt))
    part2= before_space(part1)
    return float(part2)
