#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals


if __name__ == u'__main__':
    #
    # Prepara a cadeia certificadora, separando individualmente cada um
    #
    #import pdb; pdb.set_trace()
    arq_tmp1 = open('cadeia-1.pem')
    arq_tmp2 = open('cadeia-2.pem')
    arq_tmp3 = open('cadeia-3.pem')
    cadeia = u''.join(arq_tmp1.readlines())
    cadeia += u''.join(arq_tmp2.readlines())
    cadeia += u''.join(arq_tmp3.readlines())
    arq_tmp1.close()
    arq_tmp2.close()
    arq_tmp3.close()
    cadeia_certificados = cadeia.split(u'-----END CERTIFICATE-----')

    #
    # Burramente, temos que salvar cada um num arquivo, para poder ler
    # no xmlsec...
    #
    i = 1
    for certificado in cadeia_certificados:
        if certificado.replace(u'\n', u'').strip() != '':
            certificado = u'-----BEGIN CERTIFICATE-----%s-----END CERTIFICATE-----\n' % certificado.split(u'-----BEGIN CERTIFICATE-----')[1]
            arq_tmp = open('certificados-candidatos/cert-' + str(i).zfill(2) + '.pem', 'w')
            arq_tmp.write(certificado)
            arq_tmp.close()
            i += 1
