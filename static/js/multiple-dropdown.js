$(document).ready(function() {
  $('#example-getting-started').multiselect({
    numberDisplayed: 1,
    includeSelectAllOption: true,
    allSelectedText: 'All Topics selected',
    nonSelectedText: 'No Topics selected',
    selectAllValue: 'all',
    selectAllText: 'Select all',
    unselectAllText: 'Unselect all',
    onSelectAll: function(checked) {
      var all = $('#example-getting-started ~ .btn-group .dropdown-menu .multiselect-all .checkbox');
      all
      // get all child nodes including text and comment
        .contents()
        // iterate and filter out elements
        .filter(function() {
          // check node is text and non-empty
          return this.nodeType === 3 && this.textContent.trim().length;
          // replace it with new text
        }).replaceWith(checked ? this.unselectAllText : this.selectAllText);
    },
    onChange: function() {
        debugger;
      var select = $(this.$select[0]);
      var dropdown = $(this.$ul[0]);
      var options = select.find('option').length;
      var selected = select.find('option:selected').length;
      var all = dropdown.find('.multiselect-all .checkbox');
      all
      // get all child nodes including text and comment
        .contents()
        // iterate and filter out elements
        .filter(function() {
          // check node is text and non-empty
          return this.nodeType === 3 && this.textContent.trim().length;
          // replace it with new text
        }).replaceWith(options === selected ? this.options.unselectAllText : this.options.selectAllText);
    }
  });

  $("#form").submit(function(e) {
    e.preventDefault();
    alert($(this).serialize());
  });
});

