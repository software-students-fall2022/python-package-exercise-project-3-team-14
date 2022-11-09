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
        ship_sizes=[1,2,3,4,5,6,19,40,50,"1","2","100","5","8","HI","hello"]
        dims=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,100,"10","20","5","6","Hi","bye"]
        
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
        dims=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        num=0
        flag=1
        for dim in dims:
            board,boardx = battleship.start_board(dim)
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
                        if boardx[i][j]==" " and board[i][j]==" ":
                            num+=1
            if num!=(dim+1)*(dim+1):
                flag=0
            num=0
        assert flag, "Error in creating starting board"

    def test_place_ship(self):
        """
        Verify that the ship was correctly placed (ship is of the correct length and on the board)
        """
        dims=[10,11,12,13,14,15,16,17,18,19,20]
        ships=[1,2,3,4,5,6,7,8,9]
        check=[0 for i in range(99)]
        vals=[]
        flag=0
        for d in dims:
            for s in ships:
                val=s
                board,boardx=battleship.start_board(d)
                boardx=battleship.place_ship(s,d,boardx)
                flag=0
                for i in range(d+1):
                    for j in range(d+1):
                        if boardx[i][j]=="*":
                            val-=1
                            while i+1<=d and boardx[i+1][j]=="*":
                                val-=1
                                i=i+1
                            while j+1<=d and boardx[i][j+1]=="*":
                                val-=1
                                j=j+1
                            
                            flag=1
                            break
                    if flag:
                        vals.append(val)
                        break        
        assert vals==check,"Ship not placed correctly"
    
    def test_game_finish(self,monkeypatch):
        flag=1
        cols=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        rows=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
        dims=[10,11,12,13,14,15,16,17,18,19,20]
        ships=[1,2,3,4,5,6,7,8,9]
        inp=[]
        for i in cols:
            for j in rows:
                inp.append(i+j)
        
        for d in dims:
            for s in ships:
                inputs = iter(inp)
                monkeypatch.setattr('builtins.input', lambda _: next(inputs))
                board,boardx=battleship.start_board(d)
                boardx=battleship.place_ship(s,d,boardx)
                ans=battleship.play(board,boardx,s,d)
                if ans==0:
                    flag=0
                    break

                

        assert flag, "Game did not complete to success"

    




