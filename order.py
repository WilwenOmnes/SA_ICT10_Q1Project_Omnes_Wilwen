from pyscript import Element

def show_summary(event=None):
    # Prevent form from reloading
    if event:
        event.preventDefault()

    # Get input values
    name = Element("name").value.strip() or "—"
    service = Element("service").value.strip() or "—"
    summary_box = Element("summary-box")

    # Prices dictionary
    prices = {
        "30-min Relaxation Massage": 300,
        "60-min Deep Tissue Massage": 600,
        "90-min Full Body Massage": 900,
        "Foot Massage": 250,
        "Head & Shoulder Massage": 200
    }

    price = prices.get(service, "N/A")

    # Build message
    message = f"""
    <h3>Order Summary</h3>
    <p><b>{name}</b> has chosen the service: <b>{service}</b></p>
    <p>Price: <b>₱{price}</b></p>
    <p>Your massage specialist will contact you soon.</p>
    """

    # Display in summary box
    summary_box.write(message)
