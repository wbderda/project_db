import mysql.connector

DB_NAME = "ihrf"

TABLES = {}
# Informacje o pracownikach sa w  employees
TABLES["employees"] = """
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    salary_amount DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;
"""
# Informacje o sponsorach sa w tabelach sponsors i sponsorships
TABLES["sponsors"] = """
CREATE TABLE sponsors (
    sponsor_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    representative_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL
) ENGINE=InnoDB;
"""

TABLES["sponsorships"] = """
CREATE TABLE sponsorships (
    sponsorship_id INT AUTO_INCREMENT PRIMARY KEY,
    sponsor_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    contribution_amount DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (sponsor_id) REFERENCES sponsors(sponsor_id)
) ENGINE=InnoDB;
"""
# Informacja o zrodlach finansowania
TABLES["funding_sources"] = """
CREATE TABLE funding_sources (
    funding_id INT AUTO_INCREMENT PRIMARY KEY,
    source_name VARCHAR(100) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE
) ENGINE=InnoDB;
"""


# Informacja o chomikach jest w hamsters
TABLES["hamsters"] = """
CREATE TABLE hamsters (
    hamster_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    birth_date DATE NOT NULL,
    retire_date DATE,
    sex ENUM('M','F') NOT NULL,
    owner_id INT NOT NULL,
    owner_name VARCHAR(100) NOT NULL,
    owner_networth DECIMAL(15,2) NOT NULL CHECK (owner_networth >= 0)
) ENGINE=InnoDB;
"""

# Informacje o organizowanych konkurencjach sa w tabeli disciplines
TABLES["disciplines"] = """
CREATE TABLE disciplines (
    discipline_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category ENUM('naturalna','formula_ch') NOT NULL,
    description VARCHAR(255)
) ENGINE=InnoDB;
"""

# Informacja o zawodach
TABLES["competitions"] = """
CREATE TABLE competitions (
    competition_id INT AUTO_INCREMENT PRIMARY KEY,
    discipline_id INT NOT NULL,
    competition_date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    spectators_stadium INT NOT NULL CHECK (spectators_stadium >= 0),
    hamster_id INT NOT NULL,
    winner_result DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (discipline_id) REFERENCES disciplines(discipline_id),
    FOREIGN KEY (hamster_id) REFERENCES hamsters(hamster_id)
) ENGINE=InnoDB;
"""

# Informacje o zakazanych substancjach i kontrolach antydopingowych sa w prohibited_substances i doping_controls
TABLES["prohibited_substances"] = """
CREATE TABLE prohibited_substances (
    substance_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
) ENGINE=InnoDB;
"""

TABLES["doping_controls"] = """
CREATE TABLE doping_controls (
    control_id INT AUTO_INCREMENT PRIMARY KEY,
    hamster_id INT NOT NULL,
    control_date DATE NOT NULL,
    substance_id INT,
    is_positive BOOLEAN NOT NULL,
    FOREIGN KEY (hamster_id) REFERENCES hamsters(hamster_id),
    FOREIGN KEY (substance_id) REFERENCES prohibited_substances(substance_id)
) ENGINE=InnoDB;
"""


def main():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="root_password"
    )

    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4")
    cursor.execute(f"USE {DB_NAME}")

    for table in TABLES.values():
        cursor.execute(table)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
