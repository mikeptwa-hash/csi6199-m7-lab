#!/bin/bash
cd ~/Desktop
openssl pkeyutl -decrypt -in message.enc -inkey myprivate.key
openssl dgst -sha256 -verify mypublic.key -signature message.sig message.txt
