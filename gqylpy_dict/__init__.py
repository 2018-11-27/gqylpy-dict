"""
─────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████───████████──████████─██████─────────██████████████─████████──████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░██──██░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░██──██░░░░██─
─██░░██████████─██░░██████░░██───████░░██──██░░████─██░░██─────────██░░██████░░██─████░░██──██░░████─
─██░░██─────────██░░██──██░░██─────██░░░░██░░░░██───██░░██─────────██░░██──██░░██───██░░░░██░░░░██───
─██░░██─────────██░░██──██░░██─────████░░░░░░████───██░░██─────────██░░██████░░██───████░░░░░░████───
─██░░██──██████─██░░██──██░░██───────████░░████─────██░░██─────────██░░░░░░░░░░██─────████░░████─────
─██░░██──██░░██─██░░██──██░░██─────────██░░██───────██░░██─────────██░░██████████───────██░░██───────
─██░░██──██░░██─██░░██──██░░██─────────██░░██───────██░░██─────────██░░██───────────────██░░██───────
─██░░██████░░██─██░░██████░░████───────██░░██───────██░░██████████─██░░██───────────────██░░██───────
─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────██░░██───────██░░░░░░░░░░██─██░░██───────────────██░░██───────
─██████████████─████████████████───────██████───────██████████████─██████───────────────██████───────
─────────────────────────────────────────────────────────────────────────────────────────────────────

Copyright (c) 2022 GQYLPY <http://gqylpy.com>. All rights reserved.

This file is licensed under the WTFPL:

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""
__version__ = 1, 0, 1
__author__ = '竹永康 <gqylpy@outlook.com>'
__source__ = 'https://github.com/gqylpy/gqylpy-dict'


class GqylpyDict(dict):

    def __new__(cls, __data__={}, **kw):
        if __data__.__class__ is dict:
            return dict.__new__(cls)

        if isinstance(__data__, (list, tuple, set, frozenset, Iterator)):
            return [cls(v) for v in __data__]

        return __data__

    def __init__(self, __data__=None, **kw):
        if __data__.__class__ is dict:
            kw and __data__.update(kw)
        else:
            __data__ = kw

        for name, value in __data__.items():
            self[name] = GqylpyDict(value)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, GqylpyDict(value))

    def __hash__(self):
        """
        The first thing you have to understand is that the built-in dict object
        is unhashable. Don't be misled!

        We do this mainly so that instances of "GqylpyDict" can be able to be
        added to instance of "set". Ignore the hash check and always check that
        the values are equal.

        Background story: https://github.com/gqylpy/gqylpy-dict/issues/7
        """
        return -2

    def deepget(
            self,
            keypath:  str,
            default: 'Optional[Any]'      = None,
            *,
            ignore:  'Union[list, tuple]' = None
    ) -> 'Any':
        """
        @param keypath: Hierarchy keys, use "." connection.
        @param default: Default return value if the keypath does not found.
        @param ignore:  Use a list or tuple to specify one or more undesired
                        return values. If the return value is undesired, it is
                        ignored and the default value is returned.

            >>> d = gdict({'a': [{'b': 'B'}]})
            >>> d.deepget('a[0].b')
            'B'
            >>> d.deepget('a[0].c', 'C')
            'C'
        """

    def deepset(self, keypath: str, value: 'Any') -> None:
        """
        @param keypath: Hierarchy keys, use "." connection.
        @param value:   Will set in self, according to keypath.

            >>> d = gdict({'a': [{'b': 'B'}]})

            >>> d.deepset('a[0].c', 'C')
            >>> d
            {'a': [{'b': 'B', 'c': 'C'}]}

            >>> d.deepset('d[1].f', 'F')
            >>> d
            {'a': [{'b': 'B', 'c': 'C'}], 'd': [None, {'f': 'F'}]}
        """

    def deepsetdefault(self, keypath: str, value: 'Any') -> 'Any':
        """
        @param keypath: Hierarchy keys, use "." connection.
        @param value:   Will set in self, if keypath not found.

            >>> d = gdict({'a': [{'b': 'B'}]})

            >>> d.deepsetdefault('a[0].b', 'X')
            'B'
            >>> d.deepsetdefault('a[0].c', 'X')
            'X'

            >>> d
            {'a': [{'b': 'B', 'c': 'X'}]}
        """

    def deepcontain(self, keypath: str) -> bool:
        """
        @param keypath: Hierarchy keys, use "." connection.

            >>> d = gdict({'a': [{'b': 'B'}]})
            >>> d.deepcontain('a[0].b')
            True
            >>> d.deepcontain('a[0].c')
            False
        """

    @classmethod
    def getdeep(
            cls,
            data:     dict,
            keypath:  str,
            default: 'Optional[Any]'      = None,
            *,
            ignore:  'Union[list, tuple]' = None
    ) -> 'Any':
        """
        "getdeep" based on "deepget", and is provided for built-in dict. If you
        want to use "deepget" but don't want to or can't give up the original
        data, can use "getdeep".

        @param data:    Expectation is a multilevel dict.
        @param keypath: Hierarchy keys, use "." connection.
        @param default: Default return value if the keypath does not found.
        @param ignore:  Use a list or tuple to specify one or more undesired
                        return values. If the return value is undesired, it is
                        ignored and the default value is returned.

            >>> d = {'a': [{'b': 'B'}]}
            >>> gdict.getdeep(d, 'a[0].b')
            'B'
            >>> gdict.getdeep(d, 'a[0].c', 'C')
            'C'
        """
        return cls.deepget(data, keypath, default, ignore=ignore)

    @classmethod
    def setdeep(cls, data: dict, keypath: str, value: 'Any') -> None:
        """
        "setdeep" based on "deepset", and is provided for built-in dict. If you
        want to use "deepset" but don't want to or can't give up the original
        data, can use "setdeep".

        @param data:    Expectation is a multilevel dict.
        @param keypath: Hierarchy keys, use "." connection.
        @param value:   Will set in self, according to keypath.

            >>> d = {'a': [{'b': 'B'}]}

            >>> gdict.setdeep(d, 'a[0].c', 'C')
            >>> d
            {'a': [{'b': 'B', 'c': 'C'}]}

            >>> gdict.setdeep(d, 'd[1].f', 'F')
            >>> d
            {'a': [{'b': 'B', 'c': 'C'}], 'd': [None, {'f': 'F'}]}
        """
        cls.deepset(data, keypath, value)


class _xe6_xad_x8c_xe7_x90_xaa_xe6_x80_xa1_xe7_x8e_xb2_xe8_x90_x8d_xe4_xba_x91:
    __import__(f'{__name__}.g {__name__[7:]}')
    globals()['GqylpyDict'] = globals()[f'g {__name__[7:]}'].GqylpyDict


gdict = GqylpyDict

from typing import Iterator, Any, Union, Optional
