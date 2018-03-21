import re

# Given code
class InputReader():
  def __init__(self):
    self.username = ""
    self.password = ""
    self.credentials = ""

  def readInput(self):
    self.username = raw_input("Username: ")
    self.password = raw_input("Password: ")
    self.credentials = self.username + ", " + self.password

  def getCredentials(self):
    return self.credentials


# Student solution
class CredentialWriter():
  def __init__(self, line=""):
    self.line = line

  def credentialValidator(self):
    badChars = re.findall(r"[%^&\d]", self.line)
    if len(badChars) > 0:
      return False
    else:
      return True

  def writeLine(self):
    if self.credentialValidator():
      file = open("human_login.csv", "a")
    else:
      file = open("bot_login.csv", "a")
    file.write(self.line + "\n")
    file.close()

# Instantiate InputReader class
ir = InputReader()

# Read input from the user
ir.readInput()

# Pass credentials into the __init__ method when we instantiate a CredentialWriter object
cr = CredentialWriter(ir.getCredentials())

# Call the method to write to the sppropriate file
cr.writeLine()
