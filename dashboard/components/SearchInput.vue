<template>
    <div class="select-dropdown">
        <ul class="dropdown" v-bind:class="classObject" @blur="onBlur">
            <li class="dropdown-li">
                <a href="javascript:void(0)" @click="onClick" data-value="">Select</a>
            </li>

            <li class="dropdown-li">
                <div class="addon-field">
                    <i class="icon-magnifier"></i>
                    <input
                        type="text"
                        ref="searchInput"
                        v-model="searchText"
                        @focus="onFocus"
                        @keydown.up="prevResult"
                        @keydown.down="nextResult"
                        @keydown.prevent.enter="selectResult"
                        placeholder="Start typing..."
                    />
                </div>
            </li>

            <!-- <li
                v-for="(option, index) in filteredOptions"
                class="dropdown-li"
                v-bind:class="{ selected: current == option[optionKey], hover: hoveredIndex == index }"
            >
                <a href="javascript:void(0)" @click="onClick" :data-index="index" :data-value="option[optionKey]">
                    {{ option[optionValue] }}
                </a>
            </li> -->
        </ul>
    </div>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
        },
        options: {
            type: [Object, Array],
            required: true,
        },
        optionKey: {
            type: String,
            default: 'id',
        },
        optionValue: {
            type: String,
            default: 'value',
        },
        orderBy: {
            type: [String],
            default: 'value',
        },
        selected: {
            type: [String, Number],
            default: '',
        },
    },

    data() {
        return {
            isOpen: false,
            current: this.selected,
            hoveredIndex: 0,
            searchText: '',
        };
    },

    computed: {
        orderedOptions() {
            return _.orderBy(this.options, this.orderBy);
        },
        filteredOptions() {
            let vm = this;
            return this.orderedOptions.filter(function (option) {
                return option[vm.optionValue].toUpperCase().includes(vm.searchText.toUpperCase());
            });
        },
        classObject() {
            return {
                open: this.isOpen,
            };
        },
    },

    watch: {
        current: function (val) {
            this.$emit('clicked', { key: this.name, value: this.current });
            this.searchText = '';
        },
        selected: function () {
            this.current = this.selected;
        },
    },

    methods: {
        onFocus() {
            this.isOpen = true;
        },
        onBlur() {
            this.isOpen = false;
        },
        onClick(e) {
            if (this.isOpen) {
                this.current = e.target.getAttribute('data-value');
                this.isOpen = false;
            } else {
                this.isOpen = true;
                this.$refs.searchInput.focus();
            }
        },
        nextResult(e) {
            if (this.hoveredIndex === this.filteredOptions.length - 1) {
                return (this.hoveredIndex = 0);
            }
            this.hoveredIndex = this.hoveredIndex + 1;
        },
        prevResult() {
            if (this.hoveredIndex === 0) {
                return (this.hoveredIndex = this.filteredOptions.length - 1);
            }
            this.hoveredIndex = this.hoveredIndex - 1;
        },
        selectResult() {
            this.current = Number(this.filteredOptions[this.hoveredIndex].id);
            this.isOpen = false;
        },
    },
};
</script>

<style>
.select-dropdown {
    min-height: 43px;
    min-width: 400px;
    max-width: 100%;
    position: relative;
}
ul.dropdown {
    width: 100%;
    height: auto;
    min-height: 43px;
    max-height: 300px;
    padding: 0;
    margin: 0;
    position: absolute;
    overflow: auto;
    list-style: none;
    z-index: 1;
}
ul.dropdown:after {
    content: ' ';
    height: 0;
    position: absolute;
    top: 18px;
    right: 10px;
    width: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    z-index: 19;
}
ul.dropdown li.dropdown-li {
    border-width: 0 1px 1px;
    cursor: pointer;
    display: block;
    position: absolute;
    transition: background 0.2s ease-out;
    top: 0;
    left: 0;
    padding: 0;
    width: 100%;
}
ul.dropdown li.dropdown-li:first-child {
    z-index: 2;
}
ul.dropdown li.dropdown-li.selected {
    z-index: 18;
}
ul.dropdown li.dropdown-li input {
    border: none;
    margin: 0;
}
ul.dropdown li.dropdown-li a,
ul.dropdown li.dropdown-li input[type='text'] {
    color: currentColor;
    display: block;
    padding: 9px 6px;
}
ul.dropdown.open {
    z-index: 2;
}
ul.dropdown.open li {
    position: relative;
}
</style>
