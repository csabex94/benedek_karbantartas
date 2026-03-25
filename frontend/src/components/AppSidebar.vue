<script setup lang="ts">
import type { SidebarProps } from '@/components/ui/sidebar';
import { GalleryVerticalEnd, Minus, Plus } from "lucide-vue-next";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible';
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarRail,
} from '@/components/ui/sidebar';

const props = defineProps<SidebarProps>()

// This is sample data.
const data = {
  navMain: [
    {
      title: "Nyomtatók",
      url: "#",
      items: [
        {
          title: "Irodák",
          url: "#",
        },
        {
          title: "Cimkeszerkesztő",
          url: "#",
        },
        {
          title: "Raktár",
          url: "#",
        },
        {
          title: "Száritók",
          url: "#",
        },
        {
          title: "Fagzasztóház",
          url: "#",
        },
      ],
    }
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton size="lg" as-child>
            <a href="#">
              <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <GalleryVerticalEnd class="size-4" />
              </div>
              <div class="flex flex-col gap-0.5 leading-none">
                <span class="font-medium">Arterimpex SRL.</span>
              </div>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    
    </SidebarHeader>
    <SidebarContent>
      <SidebarGroup>
        <SidebarMenu>
          <Collapsible
            v-for="(item, index) in data.navMain"
            :key="item.title"
            :default-open="index === 1"
            class="group/collapsible"
          >
            <SidebarMenuItem>
              <CollapsibleTrigger as-child>
                <SidebarMenuButton>
                  {{ item.title }}
                  <Plus class="ml-auto group-data-[state=open]/collapsible:hidden" />
                  <Minus class="ml-auto group-data-[state=closed]/collapsible:hidden" />
                </SidebarMenuButton>
              </CollapsibleTrigger>
              <CollapsibleContent v-if="item.items.length">
                <SidebarMenuSub>
                  <SidebarMenuSubItem v-for="childItem in item.items" :key="childItem.title">
                    <SidebarMenuSubButton
                      as-child
                      :is-active="false"
                    >
                      <a :href="childItem.url">{{ childItem.title }}</a>
                    </SidebarMenuSubButton>
                  </SidebarMenuSubItem>
                </SidebarMenuSub>
              </CollapsibleContent>
            </SidebarMenuItem>
          </Collapsible>
        </SidebarMenu>
      </SidebarGroup>
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
