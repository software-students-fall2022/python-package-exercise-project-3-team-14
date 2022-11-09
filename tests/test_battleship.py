from src.dailydose import battleship


class Tests:

    #
    # Test functions
    #

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_get_default(self):
        """
        Verify get() function and make sure it returns the correct starting board.
        """
        flag=1;
        ship_sizes=[1,2,3,4,5,6,19,40,50]
        dims=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,100]
        
        for s in ship_sizes:
            for d in dims:
                ship_size,dim = battleship.get(s,d)
                if ship_size>dim or dim>20:
                    flag=0
        assert flag,"Wrong initialization of ship size and dimension"

        

    
    def test_start_board(self):
        """
        Verify that both boards are correctly set up
        """
        ship_sizes=[1,2,3,4,5]
        dims=[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        num=0
        flag=1
        for ship_size in ship_sizes:
            for dim in dims:
                board,boardx = battleship.start_board(ship_size,dim)
                for i in range(dim+1):
                    for j in range(dim+1):
                        if j==0:
                            if i==0:
                                if boardx[i][j]==" " and board[i][j]==" ":
                                    num+=1
                            else:
                                if boardx[i][j]==i-1 and board[i][j]==i-1:
                                    num+=1
                        elif i==0:
                            if boardx[i][j]==chr(ord('A')+j-1) and board[i][j]==chr(ord('A')+j-1):
                                num+=1
                        else:
                            if boardx[i][j]==" " and boardx[i][j]==" ":
                                num+=1
                if num!=dim*dim:
                    flag=0
                num=0
        assert flag, "Error in creating starting board"

    def test_place_ship(self):
        """
        Verify that the ship was correctly placed
        """
        ship_size=4
        dim=10
        ship_placed=4
    
    def test_game_finish(self):
        ...
    




