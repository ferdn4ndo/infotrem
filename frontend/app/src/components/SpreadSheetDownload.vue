<template>
  <button-icon-small
    icon="download"
    text="Download"
    @click="download"
  />
</template>

<script>
  import XLSX from "xlsx";
  import ButtonIconSmall from "@/components/ButtonIconSmall";

  export default {
    components: {
      ButtonIconSmall,
    },

    props: {
      columns: {
        type: Array,
        default: () => {
          return [];
        },
      },

      data: {
        type: Array,
        required: true,
      },

      title: {
        type: String,
        required: true,
      },

      filename: {
        type: String,
        default: `export_${Math.floor(Date.now() / 1000)}.xlsx`,
      },
    },

    data() {
      return {
        sheetName: this.title,
        sheets: [{ name: "SheetOne", data: this.data }],
      };
    },

    methods: {
      download() {
        if (this.columns.length === 0) {
          console.log("No columns!");
          return;
        }

        if (this.data.length === 0) {
          console.log("No data!");
          return;
        }

        let newXlsHeader = [];
        this.columns.forEach((value) => {
          newXlsHeader.push(value.title);
        });

        let createXLSLFormatObj = [];
        createXLSLFormatObj.push(newXlsHeader);

        this.data.forEach((row) => {
          let innerRowData = [];

          this.columns.forEach((col) => {
            if (
              col.hasOwnProperty("displayCallback") &&
              col.displayCallback &&
              typeof col.displayCallback === "function"
            ) {
              innerRowData.push(
                col.displayCallback(this.getRowFieldValue(row, col.field))
              );
            } else {
              innerRowData.push(this.getRowFieldValue(row, col.field));
            }
          });

          createXLSLFormatObj.push(innerRowData);
        });

        let book = XLSX.utils.book_new();
        let sheet = XLSX.utils.aoa_to_sheet(createXLSLFormatObj);
        XLSX.utils.book_append_sheet(book, sheet, this.title);
        XLSX.writeFile(book, this.filename);
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
