<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import {computed} from 'vue';
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import {
  Field,
  FieldGroup,
  FieldLabel
} from '@/components/ui/field'
import { Input } from '@/components/ui/input'

const props = defineProps<{
  class?: HTMLAttributes["class"],
  modelValue: {
    email: string | number | undefined,
    password: string | number | undefined
  }
}>()

const emits = defineEmits(["update:modelValue", "submit:form"]);

const form = computed({
  get() {
    return props.modelValue;
  },
  set(value: string | number | undefined) {
    emits("update:modelValue", value)
  }
});

</script>

<template>
  <form :class="cn('flex flex-col gap-6', props.class)">
    <FieldGroup>
      <div class="flex flex-col items-center gap-1 text-center">
        <h1 class="text-2xl font-bold">
          Login to your account
        </h1>
        <p class="text-muted-foreground text-sm text-balance">
          Enter your email below to login to your account
        </p>
      </div>
      <Field>
        <FieldLabel for="email">
          Email
        </FieldLabel>
        <Input v-model="form.email" id="email" type="email" placeholder="m@arterimpex.ro" required />
      </Field>
      <Field>
        <div class="flex items-center">
          <FieldLabel for="password">
            Password
          </FieldLabel>
          <a
            href="#"
            class="ml-auto text-sm underline-offset-4 hover:underline"
          >
            Forgot your password?
          </a>
        </div>
        <Input v-model="form.password" id="password" type="password" required />
      </Field>
      <Field>
        <Button type="button" @click="emits('submit:form')">
          Login
        </Button>
      </Field>
    </FieldGroup>
  </form>
</template>
