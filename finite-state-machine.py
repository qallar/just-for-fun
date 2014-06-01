import unittest

class FSM:
    """a simple finite state machine
          states:     set of int
          alphabet:   set of char
          transition: dictionary, (int, char) -> int
          start:      int
          accept:     set of int
    """
    def __init__(self,states, alphabet, transition, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start = start
        self.accept = accept
        
    def step(self, state, letter):
        return self.transition[(state, letter)]
  
    def run(self, input_string):
        def run_iter(current_state, current_string):
            if len(current_string)==0:
                return False
            else:
                new_state = self.transition[(current_state, current_string[0])]
                remaining_string = current_string[1:]
                if (len(remaining_string)==0) and (new_state in self.accept):
                    return True
                else:
                    return run_iter(new_state, remaining_string)
        return run_iter(self.start, input_string)
        
class TestFSM(unittest.TestCase):
    
    def setUp(self):
        # Sipser, p. 34
        trans = {(1,'0'):1, (1,'1'):2, (2,'0'):3, (2,'1'):2, (3,'0'):2, (3,'1'):2}
        self.fsm = FSM({1,2,3}, {'0','1'}, trans, 1, {2})
        
    def test_step(self):
        self.assertEqual(self.fsm.step(1,'0'),1)
        self.assertEqual(self.fsm.step(1,'1'),2)
        self.assertEqual(self.fsm.step(2,'0'),3)
        self.assertEqual(self.fsm.step(2,'1'),2)
        self.assertEqual(self.fsm.step(3,'0'),2)
        self.assertEqual(self.fsm.step(3,'1'),2)
           
    def test_small(self):
        # Sipser, Ch. 1.1
        self.assertEqual(self.fsm.run('0'), False)
        self.assertEqual(self.fsm.run('1'), True)
        self.assertEqual(self.fsm.run('001011'), True)
        self.assertEqual(self.fsm.run('0010110'), False)
        
if __name__ == '__main__':
    unittest.main()
    

