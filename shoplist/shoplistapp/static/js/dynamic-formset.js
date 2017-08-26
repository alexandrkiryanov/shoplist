function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).prop("for", $(el).attr("for").replace(id_regex, replacement));
    if ($(el).attr("id")) $(el).prop("id", $(el).attr("id").replace(id_regex, replacement));
    if ($(el).attr("name")) $(el).prop("name", $(el).attr("name").replace(id_regex, replacement));
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var row = $('.dynamic-form:first').clone(true).get(0);
    $(row).insertAfter($('.dynamic-form:last'));
    $(row).find('*').each(function() {
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
    });
    $(row).find('.delete-row').click(function() {
        deleteForm(this, prefix);
    });

    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);

    return false;
}

function deleteForm(btn, prefix) {
    var dynamic_form = $(btn).parents('.dynamic-form');

    if (dynamic_form.find("input[id$=\"-id\"]").val()) {
        dynamic_form.find("input[id$=\"-DELETE\"]").prop("checked", true);
        dynamic_form.addClass('hidden');
        return false;
    }

    dynamic_form.remove();
    var forms = $('.dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i=0, formCount=forms.length; i<formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function() {
            updateElementIndex(this, prefix, i);
        });
    }
    return false;
}

function applyDynamicForm(prefix) {
    $('.add-row').click(function() {
        return addForm(this, prefix);
    });
    $('.delete-row').click(function() {
        return deleteForm(this, prefix);
    });
}