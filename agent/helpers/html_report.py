from django.http import HttpResponse

from client.models import Reservation
from property_owner.models import Property, Room


def export_html_reserved(request, type=None):
    txt_file = open('report.html', 'w')
    if type == 'property':
        txt_file.write(
            """
            <html>
            <head></head>
            <body>
                <h1 style="color:red; text-align:center">Booked Properties:</h1>
            """
        )
        for property_item in Property.objects.filter(property_status="reserved"):
            reservation = Reservation.objects.filter(property=property_item, reservation_type='property').last()
            if reservation:
                txt_file.write(
                    """
                    <p style="font-size:15pt; font-family:Sans-serif; font-weight: bold; text-align:center">{0}</p>
                    <div style="text-align:center; margin-top: 15px; background:#00ffbf; font-family:Sans-serif">
                        <p>Street Address : {1}</p>
                        <p>Address Line : {2}</p>
                        <p>Owner : {3}</p>
                        <p>Mobile  : {4}</p>
                        <p>Email : {5}</p>
                        <p>Price Per Night : {6}</p>
                        <p>Reserved By : {7}</p>
                        <p>Start Reserve Date : {8}</p>
                        <p>End Reserve Date : {9}</p>
                    </div>
                    """.format(
                        property_item.property_name,
                        property_item.street_address,
                        property_item.address_line,
                        (property_item.owner.first_name + " " + property_item.owner.last_name),
                        property_item.owner.mobile,
                        property_item.owner.email,
                        property_item.price_per_night,
                        (reservation.guest.first_name + " " + reservation.guest.last_name),
                        str(reservation.start_date),
                        str(reservation.end_date)
                    )
                )
    elif type == 'room':
        txt_file.write(
            """
            <html>
            <head></head>
            <body>
                <h1 style="color:red; text-align:center">Booked Rooms:</h1>
            """
        )
        for room_item in Room.objects.filter(room_status="reserved"):
            property_item = Property.objects.get(room=room_item)
            reservation = Reservation.objects.filter(room=room_item, reservation_type='room_reserve').last()
            if reservation:
                txt_file.write(
                    """
                    <p style="font-size:15pt; font-family:Sans-serif; font-weight: bold; text-align:center">{0}</p>
                    <div style="text-align:center; margin-top: 15px; background:#00ffbf; font-family:Sans-serif">
                        <p>Property Name : {1}</p>
                        <p>Street Address : {2}</p>
                        <p>Address Line : {3}</p>
                        <p>Owner : {4}</p>
                        <p>Mobile  : {5}</p>
                        <p>Email : {6}</p>
                        <p>Price Per Night : {7}</p>
                        <p>Reserved By : {8}</p>
                        <p>Start Reserve Date : {9}</p>
                        <p>End Reserve Date : {10}</p>
                    </div>
                    """.format(
                        room_item.room_name,
                        property_item.property_name,
                        property_item.street_address,
                        property_item.address_line,
                        (property_item.owner.first_name + " " + property_item.owner.last_name),
                        property_item.owner.mobile,
                        property_item.owner.email,
                        property_item.price_per_night,
                        (reservation.guest.first_name + " " + reservation.guest.last_name),
                        str(reservation.start_date),
                        str(reservation.end_date)
                    )
                )
    txt_file.write(
        """
        </body>
        </html>
        """
    )
    txt_file.close()
    response = HttpResponse(content_type='text/html')  # create a response
    txt_file = open('report.html', 'r')
    result = txt_file.read()
    response['Content-Disposition'] = 'attachment;filename="report.html"'  # tell the browser what the file is named
    response.write(result)  # put the spreadsheet data into the response
    return response
