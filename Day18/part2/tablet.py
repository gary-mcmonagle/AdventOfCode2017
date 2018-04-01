from register import register
from program import program
class tablet:
  def __init__(self, instructions):
      self.p1 = program(instructions, 0)
      self.p2 = program(instructions, 1)


  def execute_next_instruction(self):
      self.p1.execute_instruction(self.p2)
      self.p2.execute_instruction(self.p1)

  def has_terminated(self):
      if(self.p1.get_can_exit() and self.p2.get_can_exit()):
          return True
      return False

  def get_sent(self):
      return [self.p2.get_sent(),self.p1.get_sent()]


