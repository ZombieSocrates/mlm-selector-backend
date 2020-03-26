from collections import namedtuple

HostRow = namedtuple("HostRow", ["name","date", "emp_id"])

# Just FYI, I had to look this up after loading in the chideoer records based
# on my Google Calendar history
TEST_DB_HOSTS = [
    HostRow(name = "Caralanay Cameron", date = "01/06/2020", emp_id = 3859),
    HostRow(name = "Tom Antony", date = "01/13/2020", emp_id = 31104),
    HostRow(name = "Jessica Randazza-Pade", date = "01/20/2020", emp_id = 31197),
    HostRow(name = "Peter Winter", date = "01/27/2020", emp_id = 25647),
    HostRow(name = "Ilan Brat", date = "02/03/2020", emp_id = 30934),
    HostRow(name = "Nate Tower", date = "02/10/2020", emp_id = 27391),
    HostRow(name = "Sam Becker", date = "02/17/2020", emp_id = 27962),
    HostRow(name = "Jennifer Riel", date = "02/24/2020", emp_id = 31808),
    HostRow(name = "Meredith Adams-Smart", date = "03/02/2020", emp_id = 3337),
    HostRow(name = "Chris Kucharczyk", date = "03/09/2020", emp_id = 27963),
    HostRow(name = "Jane Pak", date = "03/16/2020", emp_id = 31514),
    HostRow(name = "Amie Ninh",date = "03/23/2020", emp_id = 31843),
    HostRow(name = "Hitasha Bhatia", date = "03/30/2020", emp_id = 3480),
    HostRow(name = "Steve Schwall", date = "04/06/2020", emp_id = 99),
    HostRow(name = "Jason Chen", date = "04/13/2020", emp_id = 31006),
    HostRow(name = "James Zhou", date = "04/20/2020", emp_id = 30892)
]

DEV_DB_HOSTS = [
    HostRow(name = "Caralanay Cameron", date = "01/06/2020", emp_id = 3859),
    HostRow(name = "Tom Antony", date = "01/13/2020", emp_id = 31104),
    HostRow(name = "Jessica Randazza-Pade", date = "01/20/2020", emp_id = 31197),
    HostRow(name = "Peter Winter", date = "01/27/2020", emp_id = 25647),
    HostRow(name = "Ilan Brat", date = "02/03/2020", emp_id = 30934),
    HostRow(name = "Nate Tower", date = "02/10/2020", emp_id = 27391),
    HostRow(name = "Sam Becker", date = "02/17/2020", emp_id = 27962),
    HostRow(name = "Jennifer Riel", date = "02/24/2020", emp_id = 31808),
    HostRow(name = "Meredith Adams-Smart", date = "03/02/2020", emp_id = 3337),
    HostRow(name = "Chris Kucharczyk", date = "03/09/2020", emp_id = 27963),
    HostRow(name = "Jane Pak", date = "03/16/2020", emp_id = 31514),
    HostRow(name = "Amie Ninh",date = "03/23/2020", emp_id = 31843),
    HostRow(name = "Hitasha Bhatia", date = "03/30/2020", emp_id = 3480),
    HostRow(name = "Steve Schwall", date = "04/06/2020", emp_id = 99),
    HostRow(name = "Jason Chen", date = "04/13/2020", emp_id = 31006),
    HostRow(name = "James Zhou", date = "04/20/2020", emp_id = 30892),
    HostRow(name = "Brian Lange", date = "04/27/2020", emp_id = 25643)
]