import pluginVue from 'eslint-plugin-vue'

export default [
  // 忽略产物与依赖目录
  {
    ignores: ['dist/**', 'node_modules/**', '.vite/**'],
  },
  // Vue SFC 必备规则集（essential 已含 JS 基础校验，纯 JS 项目无需 typescript-eslint）
  ...pluginVue.configs['flat/essential'],
  {
    // 视图组件文件名常为单次（Login/Profile/My…），属合法命名，关闭多词名强制规则
    rules: {
      'vue/multi-word-component-names': 'off',
    },
  },
]