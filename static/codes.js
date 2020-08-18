function validate_postal() {
    const postal_brazil = /^(\+?\d{1,4}?[ -]?)?(\d{3}[ -]?)\d{3}[ -]?\d{4}$/;
    const postal = document.getElementById("postal");
    console.log("validate");
    phone_input.value = phone_input.value.trim();
    if (phone_re.test(phone_input.value)) {
        phone_input.className = "correct";
    } else if(error_count>2){
      phone_input.className += " error_big";
        // phone_input.classList.add("error");
        // phone_input.classList.add("error_big");
    }else{
      phone_input.className = "error";
      error++;
      document.write("<p>no no no</p>");
    }

}
