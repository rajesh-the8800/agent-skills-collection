---
name: form-handling-validation
description: Manages user input, validation, and form submission handling in UI
metadata:
  version: 1.0.0
---

## Provides

- Input validation rules
- Error messages for invalid fields
- Form submission handling
- Controlled form state management

## Use When

- Building login forms
- Signup/registration forms
- Data entry forms
- Any user input workflow

---

## Instructions

### 1. Initialize Form State

- Maintain `values` object for inputs
- Maintain `errors` object for validation errors
- Maintain `loading` state for submission

---

### 2. Handle Input Changes

- Update form state on every input change
- Clear field-level errors when user edits

---

### 3. Validate Input

- Validate required fields
- Validate formats (email, password rules)
- Return errors object

---

### 4. Handle Form Submit

1. Validate all fields  
2. If errors exist → stop submission  
3. If valid → call API  
4. Handle success and failure  
5. Update loading state  

---

## Standard Flow

```javascript
handleSubmit() {
  const errors = validate(values);

  if (Object.keys(errors).length > 0) {
    setErrors(errors);
    return;
  }

  submitForm(values);
}