package com.example.SpringBootSQL.service;

import com.example.SpringBootSQL.model.Employee;

import java.util.List;

public interface EmployeeService {

Employee saveEmployee(Employee employee);
List<Employee> getAllEmployees();
Employee getEmployeeById(Long id);
Employee updateEmployee(Employee employee, long id);
void deleteEmployee(long id);
}
