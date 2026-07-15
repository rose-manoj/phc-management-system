create table patient(
    patient_id serial primary key,
    name varchar(100) not null,
    dob date not null,
    gender gender_type not null,
    contact varchar(15),
    health_status varchar(50)
);

CREATE TABLE staff(
    staff_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(15),
    dob DATE NOT NULL,
    doj DATE NOT NULL,
    role job_role NOT NULL
);

CREATE TABLE prescription(
    prescription_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    prescription_date DATE NOT NULL,

    CONSTRAINT fk_prescription_patient
    FOREIGN KEY (patient_id)
    REFERENCES patient(patient_id)
    ON DELETE CASCADE
);