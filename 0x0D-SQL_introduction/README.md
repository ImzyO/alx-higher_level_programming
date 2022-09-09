                                                                  0x0D. SQL - Introduction
                                                                                                                              
 What is Database & SQL?:       https://www.youtube.com/watch?v=FR4QIeZaPeM
 A Basic MySQL Tutorial:        https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
 Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”):   https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php
 Basic queries: SQL and RA:     https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php
 SQL technique: functions:      https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php
 SQL technique: subqueries:     https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php
 What makes the big difference between a backtick and an apostrophe?: https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458
 MySQL Keywords and Reserved words: https://dev.mysql.com/doc/refman/5.7/en/keywords.html
 MySQL Cheat Sheet:                 https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf
 MySQL 8.0 SQL Statement Syntax:    https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html
                                
                                
                                
COMMENTS FOR SQL FILES:
                                        $ cat my_script.sql
                                        -- 3 first students in the Batch ID=3
                                        -- because Batch 3 is the best!
                                        SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
                                        $

INSTALLATION ON UBUNTU 20.04:
                                      $ sudo apt update
                                      $ sudo apt install mysql-server
                                      ...
                                      $ mysql --version
                                      mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
                                      $

Connect to your MySQL server:
                                      $ sudo mysql
                                      Welcome to the MySQL monitor.  Commands end with ; or \g.
                                      Your MySQL connection id is 11
                                      Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

                                      Copyright (c) 2000, 2021, Oracle and/or its affiliates.

                                      Oracle is a registered trademark of Oracle Corporation and/or its
                                      affiliates. Other names may be trademarks of their respective
                                      owners.

                                      Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

                                      mysql>
                                      mysql> quit
                                      Bye
                                      $

USE "CONTAINER-ON-DEMAND" TO RUN MySQL":
In the container, credentials are root/root
1. Ask for container Ubuntu 20.04
2. Connect via SSH
3. OR connect via the Web terminal
4. In the container, you should start MySQL before playing with it:

                                    $ service mysql start                                                   
                                     * Starting MySQL database server mysqld 
                                    $
                                    $ cat 0-list_databases.sql | mysql -uroot -p                               
                                    Database                                                                                   
                                    information_schema                                                                         
                                    mysql                                                                                      
                                    performance_schema                                                                         
                                    sys                      
                                    $                                
                                    
                                    
file 0: a script that lists all databases of your MySQL server.

file 1: a script that creates the database hbtn_0c_0 in your MySQL server.

file 2: a script that deletes the database hbtn_0c_0 in your MySQL server.

file 3:  a script that lists all the tables of a database in your MySQL server.

file 4: a script that creates a table called first_table in the current database in your MySQL server.

file 5: a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

file 6: a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

file 7: a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

file 8: a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

file 9: a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

file 10: a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

file 11: a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

file 12: a script that updates the score of Bob to 10 in the table second_table.

file 13: a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

file 14: a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

file 15:  a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

file 16: a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

file 100: a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

file 101: Import in hbtn_0c_0 database this table dump: download
Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

file 102: Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

file 103: Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
Write a script that displays the max temperature of each state (ordered by State name).
