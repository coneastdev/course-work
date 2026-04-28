-- database: follylane.db

INSERT INTO owner_index (owner_name, owner_title, owner_address, owner_phone_number, owner_email)
VALUES ("Wallflower", 
        "Mrs", 
        "42, Pines Road, Ledbury , Herefordshire, HR7 8BZ", 
        "01732 406732", 
        "mrs@wallflower.org");

INSERT INTO breeds (breed_name, weight_range, life_expectancy)
VALUES ("Norwegian Blue", 
        "F3.5-8KG, M6KG-10KG", 
        "12y-20y");

INSERT INTO breeds (breed_name, weight_range, life_expectancy)
VALUES ("German Shepherd", 
        "F22-32KG, M30KG-40KG", 
        "9y-13y");

INSERT INTO animals (owner_ID, breed_ID, animal_species, animal_name, animal_dob)
VALUES ("1", 
        "1", 
        "Parrot", 
        "Python",
        "12/05/2006");

INSERT INTO animals (owner_ID, breed_ID, animal_species, animal_name, animal_dob)
VALUES ("1", 
        "2", 
        "Dog", 
        "Cuddles",
        "14/11/2007");

INSERT INTO perscriptions (owner_ID, animal_ID, perscription_dispence_date, perscription_medicine, perscription_dosage)
VALUES ("1", 
        "1", 
        "16/09/2011", 
        "Eveloxcyn",
        "3 times a day");

INSERT INTO appointments (owner_ID, animal_ID, appointment_date, appointment_procedure, appointment_room)
VALUES ("1", 
        "2", 
        "21/09/2011", 
        "Neutering", 
        "1030");

INSERT INTO invoices (owner_ID, animal_ID, invoice_sell_date, invoice_service_name)
VALUES ("1", 
        "2", 
        "21/09/2011", 
        "Drugs");