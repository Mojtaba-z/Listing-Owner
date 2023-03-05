# Listing-Owner
booking hotel rooms , houses , etc with making and tracking reservations that can be managed by Real State Agent (listing owner)  
# List Of Apis:
### Property Owner:
Create Property By Owner :
  http://127.0.0.1:8000/property_owner/property/
 Method : [get, post, update]
```
Body : {
    "property_name": "property number 1",
    "property_type_id": 1,
    "property_amenities": [1],
    "room": [1],
    "street_address": "cansas street 2",
    "address_line": "street line 2",
    "country_id": 1,
    "city_id": 1,
    "zip_code": "656689",
    "price_per_night": 3000,
    "property_status": "unreserved"
}
```

Create PropertyType : http://127.0.0.1:8000/property_owner/property_type/
Method : [get, post, update]
```
Body :{
    "title": "camp"
}
```

Create Room : http://127.0.0.1:8000/property_owner/room/
Method : [get, post, update]
```
Body : {
    "room_name": "room number 2",
    "room_size": "6*6",
    "room_options_id": 4,
    "room_status": "unreserved"
}
```
Create Room Options : http://127.0.0.1:8000/property_owner/room_options/
Method : [get, post, update]
```
Body :{
    "kind_of_beds": "kind 2",
    "number_of_beds": 2,
    "capacity_of_guests": 2
}
```
Ameneties Of Property : http://127.0.0.1:8000/property_owner/amenities/
Method : [get, post, update]
```
Body:{
    "title": "balcony"
}
```
### Listings Agent :
Create Listing : http://127.0.0.1:8000/agent/agent_listings/
Method : [get, post, update]
```
Body : {
    "title": "list 1",
    "property": [1, 2]
}
```
Available Properties In A Certain Date: http://127.0.0.1:8000/agent/manage_properties/available_properties/
Method : [post]
```
Body : {
    "date": "2022-06-10"
}
```
Available Rooms In A Certain Date: http://127.0.0.1:8000/agent/manage_properties/available_rooms/
Method : [post]
```
Body : {
    "date": "2022-06-22"
}
```
- Export Booked Properties Report As a Html: http://127.0.0.1:8000/agent/manage_properties/export_reserved_properties/
+ Export Booked Rooms Report As a Html : http://127.0.0.1:8000/agent/manage_properties/export_reserved_rooms/

### Client
Make Reservation : http://127.0.0.1:8000/client/reservation/
```
Body : {
    "special_request": "i want two beds",
    "start_date": "2022-05-21 02:20:15",
    "end_date": "2022-06-21 02:20:15",
    "guest_arrival_time": "2022-05-25 02:20:15",
    "property_id": 1,
    "rooms_id": [1, 2]
}
```
### * You Can Use Listing Owner Postman Collection Export File In Your Postman Account
