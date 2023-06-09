<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';
import vRadiobutton from '@/components/radiobutton/v-radiobutton.vue';

import { computed, ref } from 'vue';

import { IOrder } from '@/store/orders/orders.interfaces';

import { useOrdersStore } from '@/store/orders/orders';
import { useAuthStore } from '@/store/auth/auth';

const ordersStore = useOrdersStore();
const authStore = useAuthStore();

import useVuelidate from '@vuelidate/core';
import { helpers, minLength, maxLength, email, numeric } from '@vuelidate/validators';

const userName = ref('');
const userSurname = ref('');
const userEmail = ref('');
const userPhone = ref('');

const userCity = ref('');
const userStreet = ref('');
const userHouse = ref('');
const userHouseIndex = ref('');

const rules = computed(() => ({
  userName: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3))
  },
  userSurname: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3))
  },
  userEmail: {
    email: helpers.withMessage('Выввели неверный email', email),
  },
  userPhone: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3)),
    numeric: helpers.withMessage('Вы можете ввести только цифры', numeric),
  },
  userCity: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3))
  },
  userStreet: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3))
  },
  userHouse: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(1))
  },
  userHouseIndex: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(1))
  },
}));

const v = useVuelidate(rules, { userName, userSurname, userEmail, userPhone, userCity, userStreet, userHouse, userHouseIndex });

const paymentTypes = ref([
  { name: 'Карта', id: 'card' },
  { name: 'Наличные', id: 'cash' },
]);
const selectedPayment = ref('');

const isCardPayment = computed(() => {
  if (selectedPayment.value === 'Карта') {
    return true;
  }
  else {
    return false;
  }
})

const createOrder = () => {
  ordersStore.setOrderInfo({
    token: authStore.credentials.token,
    first_name: userName.value,
    last_name: userSurname.value,
    email: userEmail.value,
    phoneNumber: userPhone.value,
    district: userCity.value,
    street: userStreet.value,
    house: userHouse.value,
    apartment: userHouseIndex.value,
    is_card_payment: isCardPayment.value
  } as IOrder);
};

</script>

<template>
  <div class="cartpage-form">
    <form class="cartpage-form__form" action="#" @submit.prevent="">
      <div class="cartpage-form__row">
        <div class="cartpage-form__column">
          <div class="cartpage-form__title">Контактные данные</div>
          <v-input
            class="cartpage-form__input"
            label="* Ваше имя"
            name="name"
            placeholder="Введите имя"
            width="100%"
            v-model:value="v.userName.$model"
            :error="v.userName.$errors"
          />
          <v-input
            class="cartpage-form__input"
            label="* Ваша фамилия"
            name="surname"
            placeholder="Введите фамилия"
            width="100%"
            v-model:value="v.userSurname.$model"
            :error="v.userSurname.$errors"
          />
          <v-input
            class="cartpage-form__input"
            label="* Ваш email"
            name="email"
            placeholder="Введите email"
            width="100%"
            v-model:value="v.userEmail.$model"
            :error="v.userEmail.$errors"
          />
          <v-input
            class="cartpage-form__input"
            label="* Ваш телефон"
            name="phone"
            placeholder="Введите телефон"
            width="100%"
            v-model:value="v.userPhone.$model"
            :error="v.userPhone.$errors"
          />
        </div>
        <div class="cartpage-form__column">
          <div class="cartpage-form__title">Данные для доставки</div>
            <v-input
              class="cartpage-form__input"
              label="* Город"
              name="name"
              placeholder="Укажите город"
              width="100%"
              v-model:value="v.userCity.$model"
              :error="v.userCity.$errors"
            />
            <v-input
              class="cartpage-form__input"
              label="* Улица"
              name="surname"
              placeholder="Укажите улицу"
              width="100%"
              v-model:value="v.userStreet.$model"
              :error="v.userStreet.$errors"
            />
            <v-input
              class="cartpage-form__input"
              label="* Дом"
              name="email"
              placeholder="Укажите дом"
              width="100%"
              v-model:value="v.userHouse.$model"
              :error="v.userHouse.$errors"
            />
            <v-input
              class="cartpage-form__input"
              label="Корпус"
              name="phone"
              placeholder="Укажите корпус"
              width="100%"
              v-model:value="v.userHouseIndex.$model"
              :error="v.userHouseIndex.$errors"
            />
        </div>
      </div>

      <div class="cartpage-form__row">
        <div class="cartpage-form__column">
          <div class="cartpage-form__title">Способы оплаты</div>
          <div
            class="cartpage-form__radio"
            v-for="payment in paymentTypes"
            :key="payment.id">
            <vRadiobutton
              :value="payment.name"
              :label="payment.name"
              :id="payment.id"
              name="payment"
              v-model:checkedValue="selectedPayment"
            />
          </div>
        </div>
      </div>
      

      <div class="cartpage-form__row">
        <div class="cartpage-form__column cartpage-form__column_button">
          <router-link class="cartpage-form__btn" @click="createOrder" to="/make-order">Далее</router-link>
        </div>
      </div>
    </form>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.cartpage-form {
}

.cartpage-form__row {
  display: flex;
  margin: 0 -20px;
  @include for-size(tablet) {
    flex-wrap: wrap;
  }
}
.cartpage-form__column {
  width: 50%;
  padding: 0 20px;
  @include for-size(tablet) {
    width: 100%;
  }
}

.cartpage-form__input + .cartpage-form__input {
  margin-top: 50px;
}
.cartpage-form__column_button {
  width: 100%;
  padding: 0 20px;
  text-align: end;
}
.cartpage-form__title {
  @include font(36px, 400, 1.2);
  margin: 30px 0;
  @include for-size(tablet) {
    @include font(20px, 800, 1.2);
  }
}
.cartpage-form__radio {
  margin-top: 10px;
}
.cartpage-form__btn {
  @include font(32px, 400, 1.2);
  display: inline-block;
  background-color: $blue;
  color: $white;
  text-decoration: none;
  padding: 10px 25px;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
    padding: 8px 16px;
  }
}
.cartpage-form__btn::after {
  content: '>>';
  margin-left: 5px;
}
</style>