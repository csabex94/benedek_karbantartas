<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

const invoices = [
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Paid',
    totalAmount: '$250.00',
    paymentMethod: 'Credit Card',
  },
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Pending',
    totalAmount: '$150.00',
    paymentMethod: 'PayPal',
  },
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Unpaid',
    totalAmount: '$350.00',
    paymentMethod: 'Bank Transfer',
  },
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Paid',
    totalAmount: '$450.00',
    paymentMethod: 'Credit Card',
  },
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Paid',
    totalAmount: '$550.00',
    paymentMethod: 'PayPal',
  },
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Pending',
    totalAmount: '$200.00',
    paymentMethod: 'Bank Transfer',
  },
  {
    invoice: 'Konika Minolta',
    paymentStatus: 'Unpaid',
    totalAmount: '$300.00',
    paymentMethod: 'Credit Card',
  },
]
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead class="w-25">
          Model
        </TableHead>
        <TableHead class="text-right">IP Address</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="invoice in invoices" :key="invoice.invoice">
        <TableCell>
          {{ invoice.invoice }}
        </TableCell>
        <TableCell>{{ invoice.paymentStatus }}</TableCell>
        
      </TableRow>
    </TableBody>
  </Table>
</template>
