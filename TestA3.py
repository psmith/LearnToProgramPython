import unittest
import a3

class TestA3(unittest.TestCase):
    def test_is_valid_word(self):
        self.assertEquals(True, a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO'))
        
    def test_is_not_a_valid_word(self):
        self.assertEquals(False, a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TDD Sasdfkalksdjfk'))
        
    def test_make_str_from_row(self):
        self.assertEquals('ANTT', a3.make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0))
        
    def test_make_str_from_row_2(self):
        self.assertEquals('XSOB', a3.make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))
        
    def test_make_str_from_invalid_row_index(self):
        self.assertRaises(IndexError, a3.make_str_from_row, [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 3)
        
    def test_make_str_from_column_index_0(self):
        self.assertEquals('AX', a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0))
    
    def test_make_str_from_column_index_1(self):
        self.assertEquals('NS', a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))
            
    def test_make_str_from_invalid_column_index_127(self):
        self.assertRaises(IndexError, a3.make_str_from_column, [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 127)
        
    def test_board_contains_word_in_row(self):        
        self.assertTrue(a3.board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB'))
        
    def test_board_does_not_contain_word_in_row(self):        
        self.assertFalse(a3.board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'sSOB'))
    
    def test_board_contains_word_in_column(self):        
        self.assertTrue(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO'))
    
    def test_board_does_not_contain_word_in_column(self):        
        self.assertFalse(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'sSOB'))
        
    def test_board_contains_row_word(self):
        self.assertTrue(a3.board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT'))
        
    def test_board_aint_gonna_contains_word(self):
        self.assertFalse(a3.board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'OVERCOMPENSATED'))
        
    def test_board__contains_column_word(self):
        self.assertTrue(a3.board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO'))
        
    def test_no_letter_word_scores_0(self):
        self.assertEquals(0, a3.word_score(''))
        
    def test_three_letter_word_scores_3(self):
        self.assertEquals(3, a3.word_score("ANT"))
        
    def test_seven_letter_word_scores_14(self):
        self.assertEquals(14, a3.word_score('BANANAS'))
        
    def test_ten_letter_word_scores_30(self):
        self.assertEquals(30, a3.word_score('ARMADILLOS'))
        
    def test_scoring_a_players_no_point_word(self):
        playerinfo = ['Jonathan', 4]
        word = 'AT'
        a3.update_score(playerinfo, word)
        self.assertEqual(4, playerinfo[1])
        
    def test_scoring_a_players_3_point_word(self):
        playerinfo = ['Jonathan', 4]
        word = 'ANT'
        a3.update_score(playerinfo, word)
        self.assertEqual(7, playerinfo[1])
        
    def test_num_words_on_board_should_find_3(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        words = ['ANT', 'BOX', 'SOB', 'TO']
        numberOfWordsFound = a3.num_words_on_board(board, words)
        self.assertEquals(3, numberOfWordsFound)
        
    def test_num_words_on_board_should_find_0(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        words = ['BOXES']
        numberOfWordsFound = a3.num_words_on_board(board, words)
        self.assertEquals(0, numberOfWordsFound)
        
    def test_get_word_list_contains_CRUNCHY_COWS_EAT_GRASS(self):
        word_list = ['CRUNCHY','COWS','EAT', 'GRASS']
        self.assertEquals(word_list, a3.read_words(open('wordlist1.txt', 'r')))
    
    def test_get_board_contains_specified_board(self):
        board_list = [['E','F','J','A','J','C','O','W','S','S'],
                      ['S','D','G','K','S','R','F','D','F','F'],
                      ['A','S','R','J','D','U','S','K','L','K'],
                      ['H','E','A','N','D','N','D','J','W','A'],
                      ['A','N','S','D','N','C','N','E','O','P'],
                      ['P','M','S','N','F','H','H','E','J','E'],
                      ['J','E','P','Q','L','Y','N','X','D','L']]
        self.assertEquals(board_list, a3.read_board(open('board1.txt', 'r')))