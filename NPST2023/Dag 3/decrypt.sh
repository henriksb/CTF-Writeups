#!/bin/bash

openssl enc -aes-192-ctr -d -in huskeliste.txt.enc -out decrypted_file -K dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128 -iv 4867746e617466497278676265313233 | cat decrypted_file
