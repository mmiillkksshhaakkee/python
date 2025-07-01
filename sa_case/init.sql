create schema if not exists db_init;

create table employees (
    employee_id int primary key,
    full_name varchar(150) not null,
    bank_account varchar(20)
);

create table taxi_trips(
    trip_id int primary key,
    trip_datetime date not null,
    employee_id int references employees(employee_id),
    start_time timestamp not null,
    end_time timestamp,
    route_description text check ( char_length(route_description) <= 200 ),
    amount decimal(10, 2) not null,
    status varchar(20),
    status_description varchar(100)
);

create table payments(
    payment_id int primary key,
    employee_id int references employees(employee_id),
    total_amount decimal(10, 2),
    payment_status varchar(20),
    payment_datetime timestamp,
    payment_receipt text,
    payment_uploaded_datetime timestamp not null
);

create index if not exists idx_taxi_trips_employee on taxi_trips(employee_id);

create index if not exists idx_taxi_trips_status_date on taxi_trips(status, trip_datetime);

create index if not exists idx_payments_status on payments(payment_status);

-- Сумма к оплате по сотрудникам за июнь 2024
SELECT
    e.full_name,
    SUM(t.amount) AS total_amount
FROM
    taxi_trips t
JOIN
    employees e ON t.employee_id = e.employee_id
WHERE
    t.trip_date BETWEEN '2024-06-01' AND '2024-06-30'
    AND t.status = 'approved'
GROUP BY
    e.employee_id;

select e.full_name, sum(t.amount) as total_amt
from taxi_trips t
join
    employees e on t.employee_id = e.employee_id
where
    t.trip_datetime between '2025-05-01' and '2025-05-31' and status='approved'
group by e.employee_id;
