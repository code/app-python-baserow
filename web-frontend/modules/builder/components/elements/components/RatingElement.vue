<template>
  <Rating
    class="rating-element"
    :value="resolvedValue"
    :max-value="element.max_value"
    :custom-color="resolveColor(element.color, colorVariables)"
    :rating-style="element.rating_style || 'star'"
    read-only
    show-unselected
  />
</template>

<script>
import Rating from '@baserow/modules/database/components/Rating'
import formElement from '@baserow/modules/builder/mixins/formElement'
import { ensurePositiveInteger } from '@baserow/modules/core/utils/validator'

export default {
  name: 'RatingElement',
  components: {
    Rating,
  },
  mixins: [formElement],
  computed: {
    resolvedValue() {
      try {
        return ensurePositiveInteger(this.resolveFormula(this.element.value))
      } catch {
        return 0
      }
    },
  },
}
</script>
