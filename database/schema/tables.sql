create table patient(
    patient_id serial primary key,
    name varchar(100) not null,
    dob date not null,
    gender gender_type not null,
    contact varchar(15),
    health_status varchar(50)
);