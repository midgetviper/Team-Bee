CREATE DATABASE IF NOT EXISTS heroku_4e232ea7b3dda54;
USE heroku_4e232ea7b3dda54;

DROP TABLE IF EXISTS Incidents;
DROP TABLE IF EXISTS MedicineTakenEvents;
DROP TABLE IF EXISTS MedicineAssignment;
DROP TABLE IF EXISTS PatientActivationCode;
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS SessionTokens;
DROP TABLE IF EXISTS Caretaker;

CREATE TABLE Caretaker (
    email VARCHAR(30),
    password VARCHAR(30) NOT NULL,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY(email)
);

CREATE TABLE SessionTokens (
    token VARCHAR(20),
    email VARCHAR(30),
    PRIMARY KEY (token),
    FOREIGN KEY (email) REFERENCES Caretaker(email)
);

CREATE TABLE Patient (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    phoneNumber VARCHAR(20) NOT NULL
);

CREATE TABLE PatientActivationCode (
    code VARCHAR(20),
    patientId INT,
    PRIMARY KEY(code),
    FOREIGN KEY (patientId) REFERENCES Patient(id)
);

CREATE TABLE MedicineAssignment (
    name VARCHAR(30),
    patientId INT,
    PRIMARY KEY (name, patientId),
    firstIntake INT NOT NULL,
    secondIntake INT,
    thirdIntake INT,
    fourthIntake INT,
    FOREIGN KEY (patientId) REFERENCES Patient(id)
);

CREATE TABLE MedicineTakenEvents (
    patientId INT,
    timestamp TIMESTAMP,
    PRIMARY KEY (patientId, timestamp)
);

CREATE TABLE Incidents (
    patientId INT,
    timestamp TIMESTAMP,
    pickedUpCall BOOLEAN,
    PRIMARY KEY (patientId),
    FOREIGN KEY (patientId) REFERENCES Patient(id)
);