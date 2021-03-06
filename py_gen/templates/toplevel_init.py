:: # Copyright 2013, Big Switch Networks, Inc.
:: #
:: # LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
:: # the following special exception:
:: #
:: # LOXI Exception
:: #
:: # As a special exception to the terms of the EPL, you may distribute libraries
:: # generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
:: # that copyright and licensing notices generated by LoxiGen are not altered or removed
:: # from the LoxiGen Libraries and the notice provided below is (i) included in
:: # the LoxiGen Libraries, if distributed in source code form and (ii) included in any
:: # documentation for the LoxiGen Libraries, if distributed in binary form.
:: #
:: # Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
:: #
:: # You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
:: # a copy of the EPL at:
:: #
:: # http://www.eclipse.org/legal/epl-v10.html
:: #
:: # Unless required by applicable law or agreed to in writing, software
:: # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
:: # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
:: # EPL for the specific language governing permissions and limitations
:: # under the EPL.
::
:: include('_copyright.py')
:: import loxi_globals
:: include('_autogen.py')

version_names = {
:: for v in loxi_globals.OFVersions.all_supported:
    ${v.wire_version}: "${v.version}",
:: #endfor
}

def protocol(ver):
    """
    Import and return the protocol module for the given wire version.
    """
:: for v in loxi_globals.OFVersions.all_supported:
    if ver == ${v.wire_version}:
        import of${v.version.replace('.', '')}
        return of${v.version.replace('.', '')}

:: #endfor
    raise ValueError

class ProtocolError(Exception):
    """
    Raised when failing to deserialize an invalid OpenFlow message.
    """
    pass

class Unimplemented(Exception):
    """
    Raised when an OpenFlow feature is not yet implemented in PyLoxi.
    """
    pass

def unimplemented(msg):
    raise Unimplemented(msg)

class OFObject(object):
    """
    Superclass of all OpenFlow classes
    """
    def __init__(self, *args):
        raise NotImplementedError("cannot instantiate abstract class")

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)
