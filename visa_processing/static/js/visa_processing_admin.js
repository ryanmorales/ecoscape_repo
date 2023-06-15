(function($) {
    $(document).ready(function() {
        // Find the dependent field and the field to disable
        const dependentField = $('#id_visa_type');  // Replace 'id_dependent_field' with the actual ID of the dependent field
        const fieldToDisable = $('#id_non_immigrant_visa_type');  //

        //var dependentField = $('[data-dependency="visa_type"]');  // Replace 'field_to_disable' with the actual name of the field
        //var fieldToDisable = $('#id_non_immigrant_visa_type');  // Replace 'field_to_disable' with the actual name of the field

        console.log("RYANM")

        // Disable or enable the field based on the dependent field value
        function toggleFieldDisable() {
            if (dependentField.val() === 'Immigrant') {
                fieldToDisable.prop('disabled', true);
            } else {
                fieldToDisable.val() == "N/A";
                fieldToDisable.prop('disabled', false);
            }
        }

        // Initially toggle the field's disable state
        toggleFieldDisable();

        // Attach an event listener to the dependent field
        dependentField.change(function() {
            toggleFieldDisable();
        });
    });
})(django.jQuery);
