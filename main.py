#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import cgi
from caesar import encrypt
from sys import argv, exit
from helpers import alpha_position, rotate_character


class Index(webapp2.RequestHandler):
    form = """
    <form method="post">
        <label>
            I want to rot13 encrypt
            <input type="text" name="old_string"/>
            this text
    </label>
    <label>Rotate by: </label>
    <input type="text" name="rot"/>
    <input type="submit" value="Encrypt"/>
    </form>
    """
    def get(self):
        #display form
        self.response.out.write(self.form)


    def post(self):
        #read user input / set as old_string
        old_string = self.request.get("old_string")
        old_string = cgi.escape(old_string)
        rot = self.request.get("rot")
        rotint = int(rot)

        #write response
        self.response.out.write("<p>" + old_string + " is the unencrypted version of your word!" + "</p>")
        new_string = encrypt(old_string, rotint)

        self.response.out.write("<p>" + new_string + " is the encrypted version of your word!" + "</p>")

        #new_string = str(old_string)
        #new_string = old_string.encrypt(old_string, 13)
        #self.response.out.write(new_string + " is the encrypted version of your word!")

        #self.response.out.write(old_string)
        #self.response.out.write(old_string)
        #self.response.write(new_string + " is the encrypted version of your word!")


app = webapp2.WSGIApplication([
    ('/', Index),
], debug=True)
