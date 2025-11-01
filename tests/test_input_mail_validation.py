"""
Test documentation link: https://docs.google.com/spreadsheets/d/1m5PbyeRgWhdzUZFkYmPZjyFC4LP-1b0k/edit?usp=sharing&ouid=100177938618106623512&rtpof=true&sd=true
			                                        Pairwise Testing

ID  Mail Address | Name in Legal | Has "@"  |	Mail Domain	 |  Domain in Legal | Has "."   |  Top Level 	|TLD within Legal 	|TLD more than
    Name           Characters      separator                    Characters        separator    Domain (TLD)    Characters         2 characters

T01 Absent	        TRUE	        FALSE	    Present	        FALSE	            FALSE	    Present	        FALSE	            FALSE
T02 Present     	FALSE	        TRUE	    Absent	        TRUE	            TRUE	    Absent	        TRUE	            TRUE
T03 Present	        TRUE	        TRUE	    Present	        TRUE	            TRUE	    Present	        FALSE	            TRUE
T04 Absent	        FALSE	        FALSE	    Absent	        FALSE	            TRUE	    Absent	        TRUE	            FALSE
T05 Present	        TRUE	        FALSE	    Absent	        FALSE	            FALSE	    Present	        TRUE	            TRUE
T06 Absent	        FALSE	        TRUE	    Present	        TRUE	            FALSE	    Absent	        FALSE	            TRUE
T07 Present	        TRUE	        TRUE	    Absent	        TRUE	            TRUE	    Absent	        FALSE	            FALSE
T08 Absent	        FALSE	        FALSE	    Present	        TRUE	            FALSE	    Present	        TRUE	            TRUE
T09 Absent	        FALSE	        TRUE	    Absent	        FALSE	            FALSE	    Present	        FALSE	            FALSE

"""