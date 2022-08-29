import os

# Loads original boot manager GPG signature keys
original_keys_object = open("keys/boot", "r")
original_keys = original_keys_object.read()
original_keys_object.close()