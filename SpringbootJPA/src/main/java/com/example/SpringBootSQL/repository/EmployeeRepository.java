package com.example.SpringBootSQL.repository;

import com.example.SpringBootSQL.model.Employee;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository<Employee, Long> {
}
