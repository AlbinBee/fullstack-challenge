// Generated by nitro

// App Config
import type { Defu } from 'defu'

import type { default as appConfig0 } from "C:/Users/bini_/OneDrive/Desktop/Projects/full-stack-challenge/dashboard/app.config";

type UserAppConfig = Defu<{}, [typeof appConfig0]>

declare module 'nitropack' {
  interface AppConfig extends UserAppConfig {}
}
    
export {}