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

CREATE TABLE lab_test(
    test_id SERIAL PRIMARY KEY,
    prescription_id INTEGER NOT NULL,
    test_type VARCHAR(100) NOT NULL,
    test_date DATE NOT NULL,
    status VARCHAR(20),
    result TEXT,

    CONSTRAINT fk_labtest_prescription
    FOREIGN KEY (prescription_id)
    REFERENCES prescription(prescription_id)
    ON DELETE CASCADE
);

CREATE TABLE dispensed_medicines(
    medicine_id SERIAL PRIMARY KEY,
    prescription_id INTEGER NOT NULL,
    medicine_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(100),
    quantity INTEGER,

    CONSTRAINT fk_medicine_prescription
    FOREIGN KEY (prescription_id)
    REFERENCES prescription(prescription_id)
    ON DELETE CASCADE
);

CREATE TABLE treats(
    treatment_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    staff_id INTEGER,
    visit_date DATE NOT NULL,
    remarks TEXT,

    CONSTRAINT fk_treats_patient
    FOREIGN KEY (patient_id)
    REFERENCES patient(patient_id),

    CONSTRAINT fk_treats_staff
    FOREIGN KEY (staff_id)
    REFERENCES staff(staff_id)
);

