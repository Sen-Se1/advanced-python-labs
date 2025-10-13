print("=" * 50)
print("PYDANTIC TUTORIAL")
print("=" * 50)

# =============================================================================
# 1. PYTHON'S DYNAMIC TYPING PROBLEM
# =============================================================================
print("\n" + "="*50)
print("1. PYTHON'S DYNAMIC TYPING PROBLEM")
print("="*50)

print("\n--- Dynamic Typing Example ---")
x = 10
print(f"x = {x}, type: {type(x)}")
x = 'hello'
print(f"x = {x}, type: {type(x)}")

print("\n--- Problem Example ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Ali", 24)
person2 = Person("Ali", "24") 

print(f"Person 1: {person1.name}, {person1.age} (type: {type(person1.age)})")
print(f"Person 2: {person2.name}, {person2.age} (type: {type(person2.age)})")

try:
    # Simulating using age as number
    future_age = person2.age + 5
except TypeError as e:
    print(f"ERROR: {e}")

# =============================================================================
# 2. HOW TO USE PYDANTIC
# =============================================================================
print("\n" + "="*50)
print("2. HOW TO USE PYDANTIC")
print("="*50)

from pydantic import BaseModel, EmailStr, field_validator

print("\n--- Basic Pydantic Model ---")
class User(BaseModel):
    name: str
    email: str
    account_id: int

# Method 1
print("\n--- Method 1 ---")
user1 = User(
    name="Salah",
    email="salah@gmail.com",
    account_id=12345
)
print(f"User 1: {user1}")
print(f"User 1 name: {user1.name}")
print(f"User 1 email: {user1.email}")
print(f"User 1 account_id: {user1.account_id}")

# Method 2
print("\n--- Method 2 ---")
user_data = {
    'name': 'Salah',
    'email': 'salah@gmail.com',
    'account_id': 12345
}
user2 = User(**user_data)
print(f"User 2: {user2}")

# =============================================================================
# 3. VALIDATING DATA WITH PYDANTIC
# =============================================================================
print("\n" + "="*50)
print("3. VALIDATING DATA WITH PYDANTIC")
print("="*50)

print("\n--- Validation Error Example ---")
try:
    user_invalid = User(name='Ali', email='alig@mailcom', account_id='hello')
    print(user_invalid)
except Exception as e:
    print(f"Validation Error: {e}")

print("\n--- Email Validation with EmailStr ---")

class UserWithEmail(BaseModel):
    name: str
    email: EmailStr
    account_id: int

print("\n--- Valid Email ---")
user_valid_email = UserWithEmail(name='Ali', email='ali@gmail.com', account_id=1234)
print(f"Valid user: {user_valid_email}")

print("\n--- Invalid Email ---")
try:
    user_invalid_email = UserWithEmail(name='Ali', email='ali', account_id=1234)
    print(user_invalid_email)
except Exception as e:
    print(f"Email Validation Error: {e}")

# =============================================================================
# 4. CUSTOM FIELD VALIDATION
# =============================================================================
print("\n" + "="*50)
print("4. CUSTOM FIELD VALIDATION")
print("="*50)

class UserWithValidation(BaseModel):
    name: str
    email: EmailStr
    account_id: int
    
    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

print("\n--- Valid Account ID ---")
user_valid_id = UserWithValidation(name='Ali', email='ali@gmail.com', account_id=1234)
print(f"Valid user: {user_valid_id}")

print("\n--- Invalid Account ID ---")
try:
    user_invalid_id = UserWithValidation(name='Ali', email='ali@gmail.com', account_id=-12)
    print(user_invalid_id)
except Exception as e:
    print(f"Custom Validation Error: {e}")

# =============================================================================
# 5. JSON SERIALIZATION
# =============================================================================
print("\n" + "="*50)
print("5. JSON SERIALIZATION")
print("="*50)

print("\n--- JSON Serialization ---")
user_json = UserWithValidation(name='Ali', email='ali@gmail.com', account_id=1234)

# Convert to JSON string
json_str = user_json.model_dump_json()
print(f"JSON string: {json_str}")

# Convert to Python dictionary
json_obj = user_json.model_dump()
print(f"Python dict: {json_obj}")

# Parse JSON back to model
print("\n--- JSON Parsing ---")
try:
    json_input = '{"name": "Ali", "email": "ali@gmail.com", "account_id": 1234}'
    user_from_json = UserWithValidation.model_validate_json(json_input)
    print(f"User from JSON: {user_from_json}")
except Exception as e:
    print(f"JSON Parsing Error: {e}")
