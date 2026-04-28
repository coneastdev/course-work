-- database: follylane.db

-- Source - https://stackoverflow.com/a/548297
-- Posted by Noah, modified by community. See post 'Timeline' for change history
-- Retrieved 2026-04-28, License - CC BY-SA 3.0

PRAGMA writable_schema = 1;
delete from sqlite_master where type in ('table', 'index', 'trigger');
PRAGMA writable_schema = 0;


CREATE TABLE owner_index
(
    owner_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_name varchar(255),
    owner_title varchar(255),
    owner_address varchar(255),
    owner_phone_number varchar(255),
    owner_email varchar(255)
);

CREATE TABLE breeds
(
    breed_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    breed_name varchar(255),
    weight_range varchar(255),
    life_expectancy varchar(255)
);

CREATE TABLE animals
(
    animal_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_ID INTEGER,
    breed_ID INTEGER,
    animal_species varchar(255),
    animal_name varchar(255),
    animal_dob varchar(255),
    FOREIGN KEY (owner_ID) REFERENCES owner_index(owner_ID),
    FOREIGN KEY (breed_ID) REFERENCES breeds(breed_ID)
);

CREATE TABLE perscriptions
(
    perscription_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_ID INTEGER,
    animal_ID INTEGER,
    perscription_dispence_date varchar(255),
    perscription_medicine varchar(255),
    perscription_dosage varchar(255),
    FOREIGN KEY (owner_ID) REFERENCES owner_index(owner_ID),
    FOREIGN KEY (animal_ID) REFERENCES animals(animal_ID)
);

CREATE TABLE appointments
(
    appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_ID INTEGER,
    animal_ID INTEGER,
    appointment_date varchar(255),
    appointment_procedure varchar(255),
    appointment_room varchar(255),
    FOREIGN KEY (owner_ID) REFERENCES owner_index(owner_ID),
    FOREIGN KEY (animal_ID) REFERENCES animals(animal_ID)
);

CREATE TABLE invoices
(
    invoice_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_ID INTEGER,
    animal_ID INTEGER,
    invoice_sell_date varchar(255),
    invoice_service_name varchar(255),
    FOREIGN KEY (owner_ID) REFERENCES owner_index(owner_ID),
    FOREIGN KEY (animal_ID) REFERENCES animals(animal_ID)
);