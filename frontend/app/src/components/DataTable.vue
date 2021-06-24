<template>
  <article class="DataTable">
    <div
      v-if="hasContent || allowCreation"
      class="DataTable-Toolbar"
    >
      <button-icon-small
        v-if="allowCreation"
        :text="creationButtonText"
        class="DataTable-ToolbarButton"
        icon="add"
        @click="createRecord"
      />

      <spread-sheet-download
        v-if="hasContent"
        :data="rows"
        :columns="downloadHeaders"
        class="DataTable-ToolbarButton"
        title="Tabela de Dados"
      />
    </div>

    <table class="DataTable-Table">
      <!-- Header -->
      <tr class="DataTable-Row">
        <template v-for="(col, index) in headers">
          <th
            :key="`header-${index}`"
            class="DataTable-Cell DataTable-Cell--header"
          >
            {{ col.title }}
          </th>
        </template>

        <th
          v-if="allowRemoval"
          class="DataTable-Cell DataTable-Cell--header"
        >
          <the-icon icon="times" />
        </th>
      </tr>

      <!-- Data -->
      <template
        v-if="hasContent"
      >
        <tr
          v-for="(row, rowIdx) in rows"
          :key="`row_${rowIdx}_${row.id}`"
          class="DataTable-Row"
        >
          <template v-for="(col, colIdx) in headers">
            <td
              :key="`row_{index}_${row.id}_col_${colIdx}_${col.field}`"
              class="DataTable-Cell DataTable-Cell--padded"
            >
              <template v-if="col.isLink">
                <a
                  class="DataTable-Link"
                  href="#"
                  @click="clickRow(row.id, $event)"
                  v-html="col.displayCallback(getRowFieldValue(row, col.field))"
                />
              </template>

              <template v-else>
                <span v-html="col.displayCallback(getRowFieldValue(row, col.field))"/>
              </template>
            </td>
          </template>

          <td
            v-if="allowRemoval"
            class="DataTable-Cell"
          >
            <the-button
              class="DataTable-RemoveButton"
              styling="danger"
              @click="clickRemove(row)"
            >
              <the-icon
                class="DataTable-RemoveIcon"
                icon="times"
              />
            </the-button>
          </td>
        </tr>
      </template>

      <tr
        v-if="!hasContent"
        class="DataTable-Row"
      >
        <td
          :colspan="columnCount"
          class="DataTable-Cell DataTable-Cell--message"
        >
          Não existem registros para exibir.
        </td>
      </tr>

      <!-- Footer/Pagination -->
      <tr
        v-if="hasContent"
        class="DataTable-Row"
      >
        <td
          :colspan="columnCount"
          class="DataTable-Cell DataTable-Cell--footer DataTable-Cell--padded"
        >
          Exibindo {{ rows.length }} de {{ rows.length }} resultado(s).
        </td>
      </tr>
    </table>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .DataTable {
    &-Toolbar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      margin-bottom: 20px;
    }

    &-ToolbarButton {
      display: inline-block;
      max-width: 200px;
    }

    &-Table {
      width: 100%;
      font-size: 12pt;
      border-collapse: collapse;
    }

    &-Row {
    }

    &-RemoveButton {
      padding: 0;
      font-size: 13pt;
      min-width: 20px;
    }

    &-RemoveIcon {
      font-size: 13pt;
    }

    &-Cell {
      border: 1px solid $color-secondary-background-mid;

      &--padded {
        padding: 0 5px;
      }

      &--header {
        font-weight: bold;
        font-size: 13pt;
        line-height: 30px;
        background-color: $background-dark-color;
        color: $foreground-light-color;
      }

      &--message {
        font-weight: bold;
        text-align: center;
      }

      &--footer {
        text-align: right;
        line-height: 30px;
      }
    }
  }
</style>

<script>
  import SpreadSheetDownload from "@/components/SpreadSheetDownload";
  import ICON_CLASS_MAP from "@/common/icons";
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";
  import ButtonIconSmall from "@/components/ButtonIconSmall";

  export default {
    name: "DataTable",

    components: { ButtonIconSmall, TheButton, TheIcon, SpreadSheetDownload },

    props: {
      headers: {
        type: Array,
        required: true,
        validator: function(value) {
          return value.every((header) => {
            return (
              header.hasOwnProperty("title") &&
              header.hasOwnProperty("field") &&
              header.hasOwnProperty("displayCallback") &&
              header.hasOwnProperty("isLink")
            );
          });
        },
      },

      rows: {
        type: Array,
        default() {
          return [];
        },
      },

      itemsPerPage: {
        type: Number,
        default: 25,
      },

      showAddButton: {
        type: Boolean,
        default: false,
      },

      addButtonText: {
        type: String,
        default: "Adicionar novo",
      },

      addButtonIcon: {
        type: String,
        default: "",
        validator: (icon) => {
          return icon === "" || icon in ICON_CLASS_MAP;
        },
      },

      allowRemoval: {
        type: Boolean,
        default: false,
      },

      removeWarningText: {
        type: String,
        default: "Aviso: esta operação não pode ser desfeita!",
      },

      allowCreation: {
        type: Boolean,
        default: false,
      },

      creationButtonText: {
        type: String,
        default: "Novo",
      },
    },

    data() {
      return {};
    },

    computed: {
      downloadHeaders() {
        return [
          {
            title: "ID",
            field: "id",
            isLink: false,
            displayCallback: (value) => {
              return value;
            },
          },
          ...this.headers,
        ];
      },

      hasContent() {
        return this.rows.length > 0;
      },

      columnCount() {
        const totalHeaders = Object.keys(this.headers).length;

        return totalHeaders + (this.allowRemoval ? 1 : 0);
      },
    },

    methods: {
      clickRow(rowId, event) {
        this.$emit("click", rowId);

        event.preventDefault();
      },

      clickRemove(row) {
        this.$emit("remove", row);
      },

      createRecord() {
        this.$emit("create");
      },

      getRowFieldValue(row, field) {
        if (field.indexOf(".") === -1) {
          return row[field];
        }

        let fields = field.split(".");

        for (let i = 0; i < fields.length; i++) {
          row = row[fields[i]];
        }

        return row;
      },
    },
  };
</script>
